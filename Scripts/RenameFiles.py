import os
'''
NOTE: Change the image directory on your computer

EXAMPLE:
dir = 'C:/Users/gurib/Desktop/Bot de clima/Imagens'
'''
os.chdir(dir)
files=os.listdir(dir)
for i in range (len(files)):
    os.rename(files[i], str(i+1)+'Amazon.gif')

'''
NOTE: Change the image directory on your computer

EXAMPLE:
os.unlink('C:\\Users\\gurib\\Desktop\\Bot de clima\\Imagens\\1Amazon.gif') #comando para deletar a imagem 
'''