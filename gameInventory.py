import csv

inventory = {'rope':1, 'gold coin':42, 'dagger':1,'torch':6, 'arrows':12 }

def display_inventory(inventory):
    print('Inventory:')
    for v,k in inventory.items():
        print("{} {}".format(k,v))
    print('Total number of items: {}'.format(sum(inventory.values())))

display_inventory(inventory)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
added_items=dragon_loot

def add_to_inventory(inventory, added_items):
    dict_to_add={}
    for i in range(len(added_items)):
       dict_to_add[added_items[i]]=added_items.count(added_items[i]) #transforming a list into a dict.
    for k,v in dict_to_add.items(): #merging two dict without value loss
        if k in inventory.keys():
            inventory[k]+=v
        else:
            inventory[k]=v

order=input('Type ascend for ascending order or descend for descending order:')

def print_table(inventory, order=None):
    ascend=sorted(inventory,key=inventory.get)
    descend=sorted(inventory,key=inventory.get,reverse=True)
    if order=='ascend':
       order=ascend
    elif order=='descend':
       order=descend
    else:
        order=inventory
    print('Inventory:\n count     item name  \n {}'.format('-'*20))
    for i in order:
        print('{:>6}   {:>10}'.format(inventory[i],i))
    print('{} \n Total number of items:{}'.format('-'*20,sum(inventory.values())))

print_table(inventory,order)
filename=input("Type a filename,you want to import:")

def import_inventory(inventory, filename):
    if filename:
        filename=filename
    else:
        filename='/home/safi/codecool/code1/test_inventory.csv'
    dict_import={}
    with open(filename,'r') as file:
        read=csv.reader(file)
        items=list(read)
        items=items[0]
        print(items)
        for i in range(len(items)):
            dict_import[items[i]]=items.count(items[i])
        print(dict_import)
        for key,value in dict_import.items():
            if key in inventory:
                inventory[key]+=value
            else:
                inventory[key]=value

import_inventory(inventory,filename)
print_table(inventory,order)

filename=input('Type a file where you want to export your stuff:')

def export_inventory(inventory, filename):
    if filename:
        filename=filename
    else:
        filename='/home/safi/codecool/code1/test_inventory_export.csv'
    with open(filename,'w') as filename:
        write=csv.writer(filename)
        for i in inventory:
            write.writerow(i.split(",")*inventory[i])

export_inventory(inventory, filename)