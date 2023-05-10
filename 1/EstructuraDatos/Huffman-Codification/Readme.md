# Huffman Tree in C++

This is going to be a Huffman codification project that will be developed as follows:
    -the code must be done in libraries where it class must be on the classname.cpp and the definition of the functions on the classname.h file
    -Make the codification
    -Output the codification
    -Output the non-huffman codification(done by assigning a he bytes 0001 b the 0010 c the 0011 and so on)
    -Output the graphyc done to encode(the huffman coding tree)
    -Compare both codifications(huffman and assygning bytes alphabetly)
    -All the outputs must be on a webpage done with react and bring the cpp with webasembly
    -In the webpage you can imput any message that is going to be encoded by both algorithms, alphabet and huffman
    -You can also add any binary code to another box inside the webpage with a binary code and i will be decoded first via alphabet and then it will be re-encoded again via huffman and output the message decoded via alphabet and also output the re-encoding

## ChatGPT Guidance Output

It sounds like you have a specific project in mind! While I can help you with some aspects of this project, such as providing guidance on how to create a Huffman coding algorithm in C++, I'm not able to write the entire project for you. However, I can give you some tips and guidance on how to approach this project.

First, let's start with the Huffman coding algorithm. Huffman coding is a lossless data compression algorithm that assigns variable-length codes to different characters based on their frequency of occurrence in the input data. The most frequently occurring characters are assigned shorter codes, while the less frequently occurring characters are assigned longer codes. This allows for efficient data compression.

## Functionalities

Class Alphabet{
    Encode;
    Decode;
};

Class Huffman{
    Encode;
    Decode;
    HuffmanTree;
    PrintHuffmanTree;
    getFrequencies;
    getCodes;
    traverseTree;
};

### Huffman Implementation

Here are the basic steps for implementing the Huffman coding algorithm in C++:

    Create a frequency table for each character in the input data. This can be done by iterating through the input data and counting the frequency of each character.

    Create a priority queue (min heap) of nodes. Each node represents a character and its frequency. Initially, the queue will contain all the nodes from the frequency table.

    Build the Huffman coding tree by repeatedly extracting the two nodes with the lowest frequency from the priority queue and creating a new node with their combined frequency. This new node is then inserted back into the priority queue. This process is repeated until there is only one node left in the queue, which is the root of the Huffman coding tree.

    Traverse the Huffman coding tree to assign variable-length codes to each character. This can be done recursively by starting at the root of the tree and assigning a '0' to each left child and a '1' to each right child.

    Encode the input data using the variable-length codes assigned to each character.

    Decode the encoded data using the Huffman coding tree.

    Once you have implemented the Huffman coding algorithm, you can move on to creating the web application with React and WebAssembly. Here are the basic steps for creating a React web application with WebAssembly:

    Create a new React application using a tool like Create React App.

    Install the Emscripten toolchain, which allows you to compile C++ code to WebAssembly.

    Write the C++ code for the Huffman coding algorithm, following the guidelines above.

    Compile the C++ code to WebAssembly using Emscripten.

    Import the WebAssembly module into your React application and use it to encode and decode input data.

    Create a webpage that allows users to input data and see the results of the Huffman coding algorithm, as well as the non-Huffman coding algorithm.

    Add a feature that allows users to input binary code and decode it using the non-Huffman coding algorithm, and then re-encode it using the Huffman coding algorithm.

### Web Implementation

Once you have implemented the Huffman coding algorithm, you can move on to creating the web application with React and WebAssembly. Here are the basic steps for creating a React web application with WebAssembly:

    Create a new React application using a tool like Create React App.

    Install the Emscripten toolchain, which allows you to compile C++ code to WebAssembly.

    Write the C++ code for the Huffman coding algorithm, following the guidelines above.

    Compile the C++ code to WebAssembly using Emscripten.

    Import the WebAssembly module into your React application and use it to encode and decode input data.

    Create a webpage that allows users to input data and see the results of the Huffman coding algorithm, as well as the non-Huffman coding algorithm.

    Add a feature that allows users to input binary code and decode it using the non-Huffman coding algorithm, and then re-encode it using the Huffman coding algorithm.

### WASM Installation: Emscripten

Clone the emsdk repo : git clone <https://github.com/emscripten-core/emsdk.git>

cd emsdk

./emsdk install latest

./emsdk activate latest

emsdk_env.bat

To compile any C or C++ code following this command:

emcc source.c or source.cpp -s WASM=1 -o source.html/js

wasm-nm source.wasm
