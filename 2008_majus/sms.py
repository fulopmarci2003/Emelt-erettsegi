with open('sms.txt', 'r') as fin:
    uzenetek = []
    sms_db = int(fin.readline().strip())
    for _ in range(sms_db):
        sor = list(map(int, fin.readline().strip().split()))
        sor.append(fin.readline().strip())
        uzenetek.append(sor)

