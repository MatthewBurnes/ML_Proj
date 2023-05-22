def getURL():
    urls = [['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/019/09/mango-low-greenline-20220119-090000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/018/05/mango-low-greenline-20220118-050000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/017/04/mango-low-greenline-20220117-040000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/016/07/mango-low-greenline-20220116-070000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/156/07/mango-low-greenline-20220605-071400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/059/11/mango-low-greenline-20220228-111200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/291/09/mango-low-greenline-20221018-091000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/326/03/mango-low-greenline-20221122-030600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/361/10/mango-low-greenline-20221227-101200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/319/09/mango-low-greenline-20221115-093600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/300/03/mango-low-greenline-20221027-032000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/248/07/mango-low-greenline-20220905-071200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/304/06/mango-low-greenline-20221031-061800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/330/09/mango-low-greenline-20221126-094000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/311/10/mango-low-greenline-20221107-104200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/191/08/mango-low-greenline-20220710-081400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/188/05/mango-low-greenline-20220707-051000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/164/10/mango-low-greenline-20220613-102400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/161/08/mango-low-greenline-20220610-084200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/154/05/mango-low-greenline-20220603-054000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/101/09/mango-low-greenline-20220411-095000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/121/04/mango-low-greenline-20220501-044400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/123/10/mango-low-greenline-20220503-103600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/111/07/mango-low-greenline-20220421-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/103/07/mango-low-greenline-20220413-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/109/09/mango-low-greenline-20220419-094200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/128/07/mango-low-greenline-20220508-072600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/133/10/mango-low-greenline-20220513-104600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/135/10/mango-low-greenline-20220515-104400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/137/04/mango-low-greenline-20220517-043800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/139/04/mango-low-greenline-20220519-040600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/147/04/mango-low-greenline-20220527-041400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/149/10/mango-low-greenline-20220529-103000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/151/04/mango-low-greenline-20220531-042400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/158/06/mango-low-greenline-20220607-065800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/166/04/mango-low-greenline-20220615-042800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/167/05/mango-low-greenline-20220616-050000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/071/09/mango-low-greenline-20220312-091400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/073/12/mango-low-greenline-20220314-120000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/074/12/mango-low-greenline-20220315-120000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/037/07/mango-low-greenline-20220206-070000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/038/05/mango-low-greenline-20220207-053400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/039/10/mango-low-greenline-20220208-100000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/040/10/mango-low-greenline-20220209-100000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/041/12/mango-low-greenline-20220210-121800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/042/09/mango-low-greenline-20220211-093400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/043/12/mango-low-greenline-20220212-122600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/044/12/mango-low-greenline-20220213-123400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/029/07/mango-low-greenline-20220129-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/333/10/mango-low-greenline-20221129-101200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/002/01/mango-low-greenline-20220102-015800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/003/03/mango-low-greenline-20220103-030000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/004/07/mango-low-greenline-20220104-070000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/005/10/mango-low-greenline-20220105-100000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/006/02/mango-low-greenline-20220106-020000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/007/06/mango-low-greenline-20220107-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/008/08/mango-low-greenline-20220108-080000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/009/12/mango-low-greenline-20220109-120000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/010/06/mango-low-greenline-20220110-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/011/07/mango-low-greenline-20220111-070600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/012/06/mango-low-greenline-20220112-060200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/013/07/mango-low-greenline-20220113-070800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/296/02/mango-low-greenline-20221023-023200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/170/04/mango-low-greenline-20220619-045200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/010/02/mango-low-greenline-20220110-021000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/030/02/mango-low-greenline-20220130-022000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/081/03/mango-low-greenline-20220322-030400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/083/08/mango-low-greenline-20220324-080000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/069/12/mango-low-greenline-20220310-120000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/067/07/mango-low-greenline-20220308-070000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/048/12/mango-low-greenline-20220217-122200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/051/04/mango-low-greenline-20220220-040600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/052/02/mango-low-greenline-20220221-024200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/054/10/mango-low-greenline-20220223-104000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/035/12/mango-low-greenline-20220204-123000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/034/12/mango-low-greenline-20220203-122600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/032/10/mango-low-greenline-20220201-103200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/033/02/mango-low-greenline-20220202-025800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/031/03/mango-low-greenline-20220131-032200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/028/02/mango-low-greenline-20220128-024200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/027/11/mango-low-greenline-20220127-112400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/022/03/mango-low-greenline-20220122-033400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/362/04/mango-low-greenline-20221228-040600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/346/10/mango-low-greenline-20221212-103600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/331/04/mango-low-greenline-20221127-043400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/328/03/mango-low-greenline-20221124-031400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/327/04/mango-low-greenline-20221123-041000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/323/08/mango-low-greenline-20221119-082000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/322/02/mango-low-greenline-20221118-020000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/318/02/mango-low-greenline-20221114-021000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/307/03/mango-low-greenline-20221103-030000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/305/10/mango-low-greenline-20221101-102000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/303/09/mango-low-greenline-20221030-092600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/297/05/mango-low-greenline-20221024-052800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/273/06/mango-low-greenline-20220930-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/272/03/mango-low-greenline-20220929-030000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/263/09/mango-low-greenline-20220920-091200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/250/10/mango-low-greenline-20220907-102400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/249/11/mango-low-greenline-20220906-110600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/243/10/mango-low-greenline-20220831-102000.hdf5', 'N']]
    return urls