import torch
tensor = torch.ones(4, 4,dtype=torch.int)
print(tensor)
print('First row: ',tensor[0])
print('First column: ', tensor[:, 0])
print('Last column:', tensor[..., -1])
tensor[:,1] = 0
print(tensor)
if torch.cuda.is_available():
  tensor = tensor.to('cuda')
  print("cuda")
else:
    print("Not")