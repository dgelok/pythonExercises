def recoverSecret(triplets):

    final = ""
    for i in triplets:
        if final.find(i[2]) == -1:
            final += i[2]
            n3index = final.index(i[2])
        else:
            n3index = final.index(i[2])
        
        if final.find(i[1]) == -1:
            final = final[:n3index] + i[1] + final[n3index:]
            n2index = final.index(i[1])
            n3index = final.index(i[2])
        else:
            n2index = final.index(i[1])
            if n2index > n3index:
                final = final.replace(i[1],'')
                final = final[:n3index] + i[1] + final[n3index:]
        
        if final.find(i[0]) == -1:
            final = final[:n2index] + i[0] + final[n2index:]
        else:
            n1index = final.index(i[0])
            n2index = final.index(i[1])
            n3index = final.index(i[2])
            if n1index > n2index:
                final = final.replace(i[0],'')
                final = final[:n2index] + i[0] + final[n2index:]
    for i in triplets:
        if final.find(i[2]) == -1:
            final += i[2]
            n3index = final.index(i[2])
        else:
            n3index = final.index(i[2])
        
        if final.find(i[1]) == -1:
            final = final[:n3index] + i[1] + final[n3index:]
            n2index = final.index(i[1])
            n3index = final.index(i[2])
        else:
            n2index = final.index(i[1])
            if n2index > n3index:
                final = final.replace(i[1],'')
                final = final[:n3index] + i[1] + final[n3index:]
        
        if final.find(i[0]) == -1:
            final = final[:n2index] + i[0] + final[n2index:]
        else:
            n1index = final.index(i[0])
            n2index = final.index(i[1])
            n3index = final.index(i[2])
            if n1index > n2index:
                final = final.replace(i[0],'')
                final = final[:n2index] + i[0] + final[n2index:]
    return final

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))