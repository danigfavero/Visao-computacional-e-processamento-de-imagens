import csv

with open('metadata.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerow(["NAME_FILE", "DATE", "CLASS", "BACKGROUND", "LIGHT", "INDOOR"])

    for classe in ["COLHER", "GARFO", "CANECA", "FACA", "PANELA", "FRIGIDEIRA", "CONTROLE REMOTO", "CALCA", "CASACO", "CAMISETA"]:
        for objeto in range(1,4):
            for fundo in ["FUNDO1", "FUNDO2", "FUNDO3"]:
                for light in ["DIA", "NOITE"]:
                    for indoor in ["INDOOR", "OUTDOOR"]:
                        for repeticao in ["a", "b", "c"]:
                            writer.writerow([str(classe) + str(objeto) + str(repeticao) + "_" + light + "_" + indoor + "_" + fundo + ".jpg", 
                                0, 
                                classe, 
                                fundo, 
                                light=="DIA", 
                                indoor=="INDOOR"])
