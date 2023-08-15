import csv

with (
    open('biostats_tab.tsv','r',newline='') as f_read,
    open('new_biostats.tsv','w',newline='',encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read,dialect='excel-tab',qouting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write,dialect='excel',delimiter=' ',quotechar='|',qouting=csv.QUOTE_MINIMAL)
    all_data = []
    for i,line in enumirate(csv_read):
        if i ==0:
            csv_write.writerow(line)
        else:
            line[2]+=1
            for j in range(2,4+1):
                line[j] = int(line[j])
            all_data.append(line)
    csv_write.writerows(all_data)
