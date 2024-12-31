import os
import shutil


# Ruta del directorio que contiene los archivos
ruta_directorio = r"C:/Sinic3/ric/"

def organizar_archivos_por_nombre(directorio):
    # Cambiar al directorio especificado
    os.chdir(directorio)
    
    # Obtener la lista de archivos en el directorio
    archivos = [f for f in os.listdir() if os.path.isfile(f)]
    
    for archivo in archivos:
        # Obtener el nombre sin la extensiOn
        nombre_base = os.path.splitext(archivo)[0]

        if nombre_base == '25019':
            nombre_base = nombre_base + '_ALBAN'
        elif nombre_base == '25035':
            nombre_base = nombre_base + '_ANAPOIMA'
        elif nombre_base == '25040':
            nombre_base = nombre_base + '_ANOLAIMA'
        elif nombre_base == '25599':
            nombre_base = nombre_base + '_APULO'
        elif nombre_base == '25053':
            nombre_base = nombre_base + '_ARBELAEZ'
        elif nombre_base == '25095':
            nombre_base = nombre_base + '_BITUIMA'
        elif nombre_base == '25123':
            nombre_base = nombre_base + '_CACHIPAY'
        elif nombre_base == '25151':
            nombre_base = nombre_base + '_CAQUEZA'
        elif nombre_base == '25154':
            nombre_base = nombre_base + '_CARMEN_DE_CARUPA'
        elif nombre_base == '25168':
            nombre_base = nombre_base + '_CHAGUANI'
        elif nombre_base == '25178':
            nombre_base = nombre_base + '_CHIPAQUE'
        elif nombre_base == '25200':
            nombre_base = nombre_base + '_COGUA'
        elif nombre_base == '25224':
            nombre_base = nombre_base + '_CUCUNUBA'
        elif nombre_base == '25245':
            nombre_base = nombre_base + '_EL_COLEGIO'
        elif nombre_base == '25258':
            nombre_base = nombre_base + '_EL_PEÑON'
        elif nombre_base == '25260':
            nombre_base = nombre_base + '_EL_ROSAL'
        elif nombre_base == '25269':
            nombre_base = nombre_base + '_FACATATIVA'
        elif nombre_base == '25279':
            nombre_base = nombre_base + '_FOMEQUE'
        elif nombre_base == '25281':
            nombre_base = nombre_base + '_FOSCA'
        elif nombre_base == '25288':
            nombre_base = nombre_base + '_FUQUENE'
        elif nombre_base == '25293':
            nombre_base = nombre_base + '_GACHALA'
        elif nombre_base == '25297':
            nombre_base = nombre_base + '_GACHETA'
        elif nombre_base == '25299':
            nombre_base = nombre_base + '_GAMA'
        elif nombre_base == '25312':
            nombre_base = nombre_base + '_GRANADA'
        elif nombre_base == '25317':
            nombre_base = nombre_base + '_GUACHETA'
        elif nombre_base == '25320':
            nombre_base = nombre_base + '_GUADUAS'
        elif nombre_base == '25326':
            nombre_base = nombre_base + '_GUATAVITA'
        elif nombre_base == '25328':
            nombre_base = nombre_base + '_GUAYABAL_DE_SIQUIMA'
        elif nombre_base == '25335':
            nombre_base = nombre_base + '_GUAYABETAL'
        elif nombre_base == '25368':
            nombre_base = nombre_base + '_JERUSALEN'
        elif nombre_base == '25372':
            nombre_base = nombre_base + '_JUNIN'
        elif nombre_base == '25386':
            nombre_base = nombre_base + '_LA_MESA'
        elif nombre_base == '25394':
            nombre_base = nombre_base + '_LA_PALMA'
        elif nombre_base == '25398':
            nombre_base = nombre_base + '_LA_PEÑA'
        elif nombre_base == '25407':
            nombre_base = nombre_base + '_LENGUAZAQUE'
        elif nombre_base == '25436':
            nombre_base = nombre_base + '_MANTA'
        elif nombre_base == '25438':
            nombre_base = nombre_base + '_MEDINA'
        elif nombre_base == '25483':
            nombre_base = nombre_base + '_NARIÑO'
        elif nombre_base == '25486':
            nombre_base = nombre_base + '_NEMOCON'
        elif nombre_base == '25489':
            nombre_base = nombre_base + '_NIMAIMA'
        elif nombre_base == '25491':
            nombre_base = nombre_base + '_NOCAIMA'
        elif nombre_base == '25518':
            nombre_base = nombre_base + '_PAIME'
        elif nombre_base == '25524':
            nombre_base = nombre_base + '_PANDI'
        elif nombre_base == '25530':
            nombre_base = nombre_base + '_PARATEBUENO'
        elif nombre_base == '25535':
            nombre_base = nombre_base + '_PASCA'
        elif nombre_base == '25580':
            nombre_base = nombre_base + '_PULI'
        elif nombre_base == '25592':
            nombre_base = nombre_base + '_QUEBRADANEGRA'
        elif nombre_base == '25594':
            nombre_base = nombre_base + '_QUETAME'
        elif nombre_base == '25596':
            nombre_base = nombre_base + '_QUIPILE'
        elif nombre_base == '25645':
            nombre_base = nombre_base + '_SAN_ANTONIO_DEL_TEQUENDAMA'
        elif nombre_base == '25653':
            nombre_base = nombre_base + '_SAN_CAYETANO'
        elif nombre_base == '25662':
            nombre_base = nombre_base + '_SAN_JUAN_DE_RIOSECO'
        elif nombre_base == '25718':
            nombre_base = nombre_base + '_SASAIMA'
        elif nombre_base == '25743':
            nombre_base = nombre_base + '_SILVANIA'
        elif nombre_base == '25769':
            nombre_base = nombre_base + '_SUBACHOQUE'
        elif nombre_base == '25777':
            nombre_base = nombre_base + '_SUPATA'
        elif nombre_base == '25779':
            nombre_base = nombre_base + '_SUSA'
        elif nombre_base == '25781':
            nombre_base = nombre_base + '_SUTATAUSA'
        elif nombre_base == '25793':
            nombre_base = nombre_base + '_TAUSA'
        elif nombre_base == '25797':
            nombre_base = nombre_base + '_TENA'
        elif nombre_base == '25805':
            nombre_base = nombre_base + '_TIBACUY'
        elif nombre_base == '25807':
            nombre_base = nombre_base + '_TIBIRITA'
        elif nombre_base == '25815':
            nombre_base = nombre_base + '_TOCAIMA'
        elif nombre_base == '25839':
            nombre_base = nombre_base + '_UBALA'
        elif nombre_base == '25841':
            nombre_base = nombre_base + '_UBAQUE'
        elif nombre_base == '25845':
            nombre_base = nombre_base + '_UNE'
        elif nombre_base == '25506':
            nombre_base = nombre_base + '_VENECIA'
        elif nombre_base == '25862':
            nombre_base = nombre_base + '_VERGARA'
        elif nombre_base == '25867':
            nombre_base = nombre_base + '_VIANI'
        elif nombre_base == '25843':
            nombre_base = nombre_base + '_VILLA_DE_SAN_DIEGO_DE_UBATE'
        elif nombre_base == '25871':
            nombre_base = nombre_base + '_VILLAGOMEZ'
        elif nombre_base == '25873':
            nombre_base = nombre_base + '_VILLAPINZON'
        elif nombre_base == '25875':
            nombre_base = nombre_base + '_VILLETA'
        elif nombre_base == '25878':
            nombre_base = nombre_base + '_VIOTA'
        elif nombre_base == '25885':
            nombre_base = nombre_base + '_YACOPI'
        elif nombre_base == '25898':
            nombre_base = nombre_base + '_ZIPACON'

        
        
        # Crear la carpeta si no existe
        if not os.path.exists(nombre_base):
            os.makedirs(nombre_base)
        
        # Mover el archivo a la carpeta correspondiente
        shutil.move(archivo, os.path.join(nombre_base, archivo))



# Ejecutar la funciOn
organizar_archivos_por_nombre(ruta_directorio)
