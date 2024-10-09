# Variables del Dataset de Complicaciones de Infarto de Miocardio

A continuación se describen las variables del dataset:

## Datos del Paciente
- **AGE**: Edad del paciente.
- **SEX**: Sexo del paciente (0 = Mujer, 1 = Hombre).

## Antecedentes y Factores de Riesgo
- **INF_ANAM**: Antecedentes de infarto de miocardio.
- **STENOK_AN**: Antecedentes de angina de pecho.
- **FK_STENOK**: Frecuencia de ataques de angina.
- **IBS_POST**: Enfermedad isquémica del corazón posterior al infarto.
- **IBS_NASL**: Enfermedad isquémica del corazón.
- **GB**: Hipertensión arterial.
- **SIM_GIPERT**: Síndrome de hipertensión.
- **DLIT_AG**: Duración de la hipertensión arterial.
- **ZSN_A**: Insuficiencia cardíaca crónica.

## Parámetros Clínicos
- **nr_01** a **nr_11**: Variables relacionadas con la evaluación neurológica del paciente (específicas del estudio).
- **np_01** a **np_10**: Variables relacionadas con parámetros fisiológicos o electrocardiográficos.

## Enfermedades Endocrinas
- **endocr_01**: Presencia de diabetes mellitus.
- **endocr_02**: Enfermedades tiroideas.
- **endocr_03**: Otras patologías endocrinas.

## Enfermedades Pulmonares
- **zab_leg_01** a **zab_leg_06**: Variables relacionadas con enfermedades pulmonares.

## Presión Arterial
- **S_AD_KBRIG**: Presión arterial sistólica medida en la brigada médica.
- **D_AD_KBRIG**: Presión arterial diastólica medida en la brigada médica.
- **S_AD_ORIT**: Presión arterial sistólica medida en la unidad de cuidados intensivos.
- **D_AD_ORIT**: Presión arterial diastólica medida en la unidad de cuidados intensivos.

## Parámetros Post Infarto
- **O_L_POST**: Parámetro relacionado con la duración o el tiempo después del infarto.
- **K_SH_POST**: Complicaciones cardiovasculares post-infarto.
- **MP_TP_POST**: Parámetros relacionados con terapias post-infarto.
- **SVT_POST**: Taquicardia supraventricular post-infarto.
- **GT_POST**: Taquicardia ventricular post-infarto.
- **FIB_G_POST**: Fibrilación post-infarto.

## Localización del Infarto
- **ant_im**: Infarto en la pared anterior del miocardio.
- **lat_im**: Infarto en la pared lateral del miocardio.
- **inf_im**: Infarto en la pared inferior del miocardio.
- **post_im**: Infarto en la pared posterior del miocardio.
- **IM_PG_P**: Presencia de un infarto mayor.

## Ritmos y Complicaciones ECG
- **ritm_ecg_p_01** a **ritm_ecg_p_08**: Parámetros de ritmo electrocardiográfico antes y después del infarto.
- **n_r_ecg_p_01** a **n_r_ecg_p_10**: Complicaciones en el ritmo cardíaco relacionadas con el electrocardiograma (ECG).

## Tratamientos
- **fibr_ter_01** a **fibr_ter_08**: Variables que indican la aplicación de diferentes terapias fibrinolíticas.
  
## Variables Relacionadas con la Sangre
- **GIPO_K**: Hipopotasemia (niveles bajos de potasio en sangre).
- **K_BLOOD**: Nivel de potasio en sangre.
- **GIPER_NA**: Hipernatremia (niveles altos de sodio en sangre).
- **NA_BLOOD**: Nivel de sodio en sangre.
- **ALT_BLOOD**: Niveles de alanina aminotransferasa (ALT) en sangre.
- **AST_BLOOD**: Niveles de aspartato aminotransferasa (AST) en sangre.
- **KFK_BLOOD**: Niveles de creatina fosfoquinasa (CPK) en sangre.
- **L_BLOOD**: Conteo de leucocitos en sangre.
- **ROE**: Velocidad de sedimentación globular (VSG).

## Otros Parámetros Relacionados
- **TIME_B_S**: Tiempo entre el inicio de los síntomas y el tratamiento.
- **R_AB_1_n** a **R_AB_3_n**: Parámetros relacionados con la respiración o el uso de antibióticos (según el contexto).
- **NA_KB**, **NOT_NA_KB**: Parámetros relacionados con niveles de sodio y otros electrolitos en sangre.
- **LID_KB**: Uso de lidocaína.
- **NITR_S**: Uso de nitratos.

## Medicación y Tratamientos Post Infarto
- **NA_R_1_n** a **NA_R_3_n**: Parámetros relacionados con el tratamiento de sodio o electrolitos.
- **NOT_NA_1_n** a **NOT_NA_3_n**: Parámetros de medicación relacionados con otros tratamientos.
- **LID_S_n**: Uso de lidocaína en tratamiento secundario.
- **B_BLOK_S_n**: Uso de betabloqueantes.
- **ANT_CA_S_n**: Uso de antagonistas de calcio.
- **GEPAR_S_n**: Uso de heparina.
- **ASP_S_n**: Uso de aspirina.
- **TIKL_S_n**: Uso de ticlopidina.
- **TRENT_S_n**: Uso de pentoxifilina.