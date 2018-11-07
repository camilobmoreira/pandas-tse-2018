from urllib.request import urlretrieve
import os
import zipfile

done = False
while not done:

    ufs = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    keep_downloading = True
    #Download the zip file from TSE website
    while keep_downloading:
        files = os.listdir('./zips')
        for uf in ufs:
            file = f'boletim_urnas_{uf}.zip'
            if file in files:
                print(file + ' exists')
                continue
            else:
                try:
                    url = f'http://agencia.tse.jus.br/estatistica/sead/eleicoes/eleicoes2018/buweb/BWEB_1t_{uf}_101020181938.zip'
                    file = f'./zips/boletim_urnas_{uf}.zip'
                    print('Downloading '+ file)
                    urlretrieve(url, file)
                except:
                    print ("Unexpected error: ", sys.exc_info()[0])
        keep_downloading = len(files) != len(ufs)



    files = os.listdir('./zips')
    extracted_files = os.listdir('./boletins')
    extracted = []
    for file in extracted_files:
        extracted.append(file.replace('bweb_1t_', '')[:2] )

    for file in files:
        if file.replace('boletim_urnas_', '').replace('.zip', '') not in extracted:
            try:
                print('Extracting '+ file)
                file = f'./zips/{file}'
                zip_ref = zipfile.ZipFile(file, 'r')
                zip_ref.extractall('./boletins')
                zip_ref.close()
            except:
                print ("Unexpected error: ", sys.exc_info()[0])
        else:
            print(file + ' already unzipped')

    extracted_files = os.listdir('./boletins')
    done = len(extracted_files) == len(ufs) + 1
