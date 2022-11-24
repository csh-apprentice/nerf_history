import torch
import numpy as np

'''

for img_id in range (5):
    path="seg_results/"+str(img_id)+str(".pt")
    seggrid=torch.load(path)
    
    inverse_path="seg_results/"+str(img_id)+str("_inverse.pt") 
    inverse_seggrid=torch.load(inverse_path)
    
    grid_sum=seggrid+inverse_seggrid
    
    one=torch.ones(grid_sum.shape,dtype=torch.float,device="cuda:0")
    grid_sum=torch.where(grid_sum>1e-6,grid_sum,one)
    
    seggrid_normalize=torch.div(seggrid,grid_sum)
    
    save_path="seg_results/"+str(img_id)+str("_normalize.pt")
    
    torch.save(seggrid_normalize,save_path)
'''
path="seg_results/"+str(0)+str("_normalize.pt")
seggrid=torch.load(path)

maxgrid=torch.zeros(seggrid.shape,device="cuda:0")

    
for img_id in range (5):
    path="seg_results/"+str(img_id)+str("_normalize.pt")
    seggrid=torch.load(path)
    maxgrid=torch.max(seggrid,maxgrid)
    
save_path="seg_results/"+str("sum_color.pt")
torch.save(maxgrid,save_path)
     
#print(an)
'''

l = torch.autograd.Variable(torch.LongTensor(2, 2).zero_())
print(l)
m1 = torch.LongTensor(1, 2, 2).random_(0, 1)
print(m1)
m2 = torch.LongTensor(1, 2, 2).random_(0, 1)
print(m2)
# compute linear index
m3 = torch.autograd.Variable(m1 * 10 + m2)  
# make ones the same size as index
values = torch.autograd.Variable(torch.LongTensor([1])).expand_as(m3)
l.put_(m3, values, accumulate=True)
print(l)

'''

