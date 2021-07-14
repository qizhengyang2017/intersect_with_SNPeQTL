import sys
# python mege_2type_eqtl.py ./example_data/SNP_eqtl.txt ./example_data/intro_eqtl.txt out.txt


eqtl_file_name = sys.argv[1]
intro_file_name = sys.argv[2]
out_file_name = sys.argv[3]

with open(eqtl_file_name) as f:
    eqtl_dic = {}
    for line in f:
        line = line.strip().split()
        gene = line[0]
        snp = line[1]
        chr = snp.split('_')[0]
        pos = snp.split('_')[1]
        p1 = line[12]
        p2 = line[16]
        
        # SNP eQTL不需要嵌套列表
        if gene in eqtl_dic.keys():
            eqtl_dic[gene] = eqtl_dic[gene] + [snp,chr,pos,p1,p2]
        else:
            eqtl_dic[gene] = [snp,chr,pos,p1,p2]
    #print(eqtl_dic)

# 读入渐渗
with open(intro_file_name) as f:
    intro_dic = {}
    for line in f:
        line = line.strip().split()
        gene = line[5]
        intro = line[0]
        chr = line[1]
        start = line[2]
        end = line[3]
        p1 = line[11]
        p2 = line[12]
        if gene in intro_dic.keys():
            intro_dic[gene] = intro_dic[gene] + [[intro,chr,start,end,p1,p2]]
        else:
            intro_dic[gene] = [[intro,chr,start,end,p1,p2]]
    #print(intro_dic)

out_file = open(out_file_name,'w')
for gene in intro_dic.keys():
    if gene in eqtl_dic.keys():
        # 遍历嵌套列表
        intro_out = []
        for seg in intro_dic[gene]:
            if int(eqtl_dic[gene][2]) >= int(seg[2]) and int(eqtl_dic[gene][2]) <= int(seg[3]):
                intro_out.append([seg[0],seg[4],seg[5]])
        # 输出
        if len(intro_out) > 0:
            snp = eqtl_dic[gene][0]
            p1 = eqtl_dic[gene][3]
            p2 = eqtl_dic[gene][4]
            out = [[gene,snp,p1,p2]] + intro_out
            # print(out)
            for list in out:
                for number in list:
                    out_file.write(number+'\t')
            out_file.write('\n')
out_file.close()


