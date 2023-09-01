# SoccerField - This is a python script to be used with Blender 3d.
# It makes a soccer field of Width x Length with all the white lines.
# I made this years ago when working selling synthetic sports turf for 
# our clients to see the dimensions of their project. 

# To use this, you must first install Blender 3D, then put this on the "Scripting"
# tab then run it with "Alt + P".

import bpy
import math

largura = 15.0                # width (m)
comprimento = 30.0            # length (m)
lateral_da_largura = 0.45     # size of the width sideline (m)
lateral_do_comprimento = 0.45 # side of the length sideline (m)
linha_branca = 0.1            # size of the white lines (m)

metade_comprimento = comprimento/2
metade_largura = largura/2
linha_pequena_da_area = comprimento/6

#CampoP
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(0.0, 0.0, 0.0))
bpy.ops.transform.resize(value=(comprimento,largura,1))

#Campo XPSC
lima = bpy.ops.material.new()
esmeralda = bpy.ops.material.new()

if math.floor(comprimento)%2 == 0: 

    #faixas internas
    for x in range(0,int(metade_comprimento)):
        bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
        location=(int(metade_comprimento)-2*(x+0.5), 0.0, 0.01))

        bpy.ops.transform.resize(value=(2,largura,0.01))

    #faixas das bordas    
    resto = comprimento%math.floor(comprimento-1)
    #Esquerda
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
    location=(-metade_comprimento+(resto-1)/4, 0.0, 0.01))

    bpy.ops.transform.resize(value=((resto-1)/2,largura,0.01))

    #Direita
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
    location=(metade_comprimento-(resto-1)/4, 0.0, 0.01))
    
    bpy.ops.transform.resize(value=((resto-1)/2,largura,0.01))

else: 
    
    #faixas internas
    for x in range(1,int(metade_comprimento)):
        bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
        location=(int(metade_comprimento)-2*x, 0.0, 0.01))

        bpy.ops.transform.resize(value=(2,largura,0.01))

    #faixas das bordas    
    resto = comprimento%math.floor(comprimento-1)
        
    if math.floor(comprimento)%2 < 1:
        menor_par = math.floor(comprimento)
        comprimento_restante = comprimento - menor_par

    else:
        menor_par = math.floor(comprimento-1)
        comprimento_restante = comprimento - menor_par
        #Esquerda
        bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
        location=(-metade_comprimento+(comprimento_restante)/2+0.5, 0.0, 0.01))

        bpy.ops.transform.resize(value=(comprimento_restante,largura,0.01))

        #Direita
        bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
        location=(metade_comprimento-(comprimento_restante)/2-0.5, 0.0, 0.01))

        bpy.ops.transform.resize(value = (comprimento_restante,largura,0.01))

    
#Linhas de Demarcação Brancas Bordas
    #Cima
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(0.0, metade_largura-lateral_do_comprimento, 0.02))
bpy.ops.transform.resize(value=(comprimento-2*lateral_da_largura + linha_branca,linha_branca,1))
    #Baixo
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(0.0, -metade_largura+lateral_do_comprimento, 0.02))
bpy.ops.transform.resize(value=(comprimento-2*lateral_da_largura + linha_branca,linha_branca,1))
    #Esquerdo
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(-metade_comprimento+lateral_da_largura, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura-2*lateral_do_comprimento + linha_branca,1))
    #Meio
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(0.0, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura-2*lateral_do_comprimento + linha_branca,1))
    #Direito
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(metade_comprimento-lateral_da_largura, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura-2*lateral_do_comprimento + linha_branca,1))

#Linhas de Demarcação Brancas Falta
    #Esquerdo
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(-2*metade_comprimento/9, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura/6,0.02))
    #Direito
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(+2*metade_comprimento/9, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura/6,0.02))

#Linhas de Demarcação Brancas Gols
    #Esquerdo Alto
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(comprimento/2 - largura/6 - lateral_da_largura - linha_branca/2, largura/4, 0.02))
bpy.ops.transform.resize(value=(largura/3,linha_branca,1))
    #Direito Alto
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(-comprimento/2 + largura/6 + lateral_da_largura + linha_branca/2, largura/4, 0.02))
bpy.ops.transform.resize(value=(largura/3,linha_branca,1))

    #Esquerdo Baixo
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(comprimento/2 - largura/6 - lateral_da_largura - linha_branca/2, -largura/4, 0.02))
bpy.ops.transform.resize(value=(largura/3,linha_branca,1))
    #Direito Baixo
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(-comprimento/2 + largura/6 + lateral_da_largura + linha_branca/2, -largura/4, 0.02))
bpy.ops.transform.resize(value=(largura/3,linha_branca,1))

    #Esquerdo
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(-comprimento/2+largura/3+lateral_da_largura, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura/2 + linha_branca,1))
    #Direito
bpy.ops.mesh.primitive_grid_add(x_subdivisions=2, y_subdivisions=2, size=1, align='WORLD', 
location=(comprimento/2-largura/3-lateral_da_largura, 0.0, 0.02))
bpy.ops.transform.resize(value=(linha_branca,largura/2 + linha_branca,1))


#Bola do Penalti
    #Direito    
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.2, 
depth=0.02, location=((comprimento/2-largura/3-lateral_da_largura+2*metade_comprimento/9)/2, 0.0, 0.02))

    #Esquerdo    
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.2, 
depth=0.02, location=(-(comprimento/2-largura/3-lateral_da_largura+2*metade_comprimento/9)/2, 0.0, 0.02))

    #Meio    
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.2, 
depth=0.02, location=(0.0, 0.0, 0.02))