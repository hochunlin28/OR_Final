# -*- coding: utf-8 -*-
from pulp import*


ss = 100000000
time_table = [
[ss,9,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,5,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[9,ss,20,29,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,5,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,20,ss,9,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,34,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,29,9,ss,26,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,26,ss,14,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,20,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,14,ss,10,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,10,ss,25,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,5,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,25,ss,10,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,10,ss,14,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,9,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,14,ss,11,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,55,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,11,ss,22,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,22,ss,6,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,30,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,6,ss,15,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,15,ss,15,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,30,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,15,ss,23,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,23,ss,25,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,23,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,25,ss,7,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,10],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,7,ss,6,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,6,ss,7,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,7,ss,7,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,7,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss],
[5,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,8,23,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,5,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,8,ss,15,ss,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,34,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,25,15,ss,13,ss,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,20,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,13,ss,11,ss,ss,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,5,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,11,ss,19,32,ss,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,9,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,19,ss,13,24,ss,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,55,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,32,13,ss,11,25,ss,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,30,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,24,11,ss,14,32,ss],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,30,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,25,14,ss,18,30],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,23,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,32,18,ss,12],
[ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,10,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,ss,30,12,ss]
]

cost_table=[
[-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[23,-1,50,72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,50,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,34,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,72,23,-1,89,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,89,-1,43,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,17,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,43,-1,35,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,35,-1,87,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,15,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,87,-1,32,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,32,-1,40,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,15,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,40,-1,33,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,38,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,33,-1,79,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,79,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,40,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,23,-1,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,54,-1,52,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,47,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,-1,87,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,87,-1,86,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,86,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,23,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,23,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,23,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,40,160,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,40,-1,130,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,34,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,160,130,-1,130,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,130,-1,140,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,140,-1,270,390,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,270,-1,130,230,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,38,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,390,130,-1,110,250,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,40,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,230,110,-1,150,420,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,47,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,250,150,-1,280,410],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,420,280,-1,140],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,410,140,-1]
]

shortest = [-1] *(32*32)
total_cost = [0] *(32*32)
path = [""] *(32*32)

for k in range(32):
    for m in range(32):
        model = pulp.LpProblem("time min", pulp.LpMinimize)
        if(k==m):
            shortest[k*32+m] = -1
            total_cost[k*32+m] = -1
            path[k*32+m] = "nop"
        elif(shortest[m*32+k]!=-1):
            shortest[k*32+m] = shortest[m*32+k]
            total_cost[k*32+m] = total_cost[m*32+k]
            path[k*32+m] = path[m*32+k]
        else:    
            x = [-1] *(32*32)

            #Add decision variable
            for i in range(32):
                for j in range(32):
                    # %(1000+i*32+j,i,j): make sure v in model.variables() is in order
                    x[i*32+j] = pulp.LpVariable('x_%d_%d_%d'%(1000+i*32+j,i,j),lowBound = 0, cat='Binary')
       
            #設置目標函數
            model += lpSum([[time_table[i][j]*x[i*32+j] for j in range(32)] for i in range(32)])

            for i in range(32):
                if i==k:
                    model += lpSum([x[i*32+j] - x[j*32+i] for j in range(32)]) == 1
                elif i==m:
                    model += lpSum([x[i*32+j] - x[j*32+i] for j in range(32)]) == -1
                else:
                    model += lpSum([x[i*32+j] - x[j*32+i] for j in range(32)]) == 0
        
            model.solve()  # mmodel.solve()求解

        # 透過屬性varValue,name顯示決策變數名字及值
            z = 0
            for v in model.variables():
            #print(v.name, "=", v.varValue)
                if(v.varValue==1):
                    path[k*32+m]+=v.name+", "
                if(cost_table[int(z/32)][int(z%32)]>=0 and int(v.varValue)>0):
                    total_cost[k*32+m] += int(v.varValue) * cost_table[int(z/32)][int(z%32)]
                z += 1
        # 透過屬性value(model.objective)顯示最佳解
            #print('obj=',value(model.objective))
            shortest[k*32+m] = value(model.objective)
"""
k=15
m=0
print('%d'%shortest[k*32+m])
print('%d'%total_cost[k*32+m])
print(path[k*32+m])
k=0
m=15
print('%d'%shortest[k*32+m])
print('%d'%total_cost[k*32+m])
print(path[k*32+m])
k=20
m=25
print('%d'%shortest[k*32+m])
print('%d'%total_cost[k*32+m])
print(path[k*32+m])
k=25
m=20
print('%d'%shortest[k*32+m])
print('%d'%total_cost[k*32+m])
print(path[k*32+m])

print('%d'%cost_table[0][21])
print('%d'%cost_table[21][23])
print('%d'%cost_table[23][24])
print('%d'%cost_table[24][25])
print('%d'%cost_table[25][26])
print('%d'%cost_table[26][28])
print('%d'%cost_table[28][30])
print('%d'%cost_table[30][15])
"""