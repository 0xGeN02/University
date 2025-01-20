import asyncio
import sys
import os
import argparse
from pathlib import Path
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

from app.db.database import Base

load_dotenv()

PROD_DATABASE_URL = os.getenv('DATABASE_URL')
TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
def get_database_url(env='prod'):
    base_url = PROD_DATABASE_URL
    if env == 'test':
        base_url = TEST_DATABASE_URL
    return base_url

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', choices=['prod', 'test'], default='test',
                      help='Environment (prod/test)')
    return parser.parse_args()

args = parse_args()
DATABASE_URL = get_database_url(args.env)
engine = create_async_engine(DATABASE_URL)

from app.db.database import Base

async def confirm_database():
    """Confirm database operation with user"""
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT current_database()"))
        db_name = result.scalar()
        print(f"\n⚠️  WARNING: About to modify database: {db_name}")
        print(f"Environment: {args.env.upper()}")
        print(f"URL: {engine.url}\n")
        if args.env == 'prod':
            if input("⚠️  This will DELETE ALL DATA in PRODUCTION. Continue? (y/N): ").lower() != 'y':
                print("Migration cancelled")
                sys.exit(0)
        else:
            if input("Continue with test database? (y/N): ").lower() != 'y':
                print("Migration cancelled")
                sys.exit(0)

async def print_current_database_tables():
    """Print current database tables"""
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        tables = result.all()
        print("\nCurrent database tables:")
        for table in tables:
            print(table[0])

async def drop_tables():
    """Drop all tables in database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def create_tables():
    """Create all tables in database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def print_current_table_content():
    """Print content of all tables in database"""
    async with engine.connect() as conn:
        # Get all tables
        result = await conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """))
        tables = result.fetchall()
        
        print("\nDatabase content:")
        print("=================")
        
        for table in tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")
            print("-" * (len(table_name) + 7))
            
            # Get table content
            result = await conn.execute(text(f"SELECT * FROM {table_name}"))
            rows = result.fetchall()
            
            if not rows:
                print("No data")
                continue
                
            # Get column names
            columns = result.keys()
            
            # Print each row
            for row in rows:
                print("\nRecord:")
                for col, value in zip(columns, row):
                    print(f"  {col}: {value}")
        
async def main():
    print(f"\nStarting migration for {args.env.upper()} environment...")
    await confirm_database()
    await print_current_database_tables()
    await print_current_table_content()
    
    await drop_tables()
    await create_tables()
    await print_current_database_tables()
    await print_current_table_content()

    print(f"\nMigration completed for {args.env.upper()} environment")

if __name__ == "__main__":
    asyncio.run(main())