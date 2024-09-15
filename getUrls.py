def getURL():
    urls = [['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/156/07/mango-low-greenline-20220605-071400.hdf5', 'Y'],
  #  ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/059/11/mango-low-greenline-20220228-111200.hdf5', 'Y'],  #need 10 y 13n
    #['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/291/09/mango-low-greenline-20221018-091000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/326/03/mango-low-greenline-20221122-030600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/128/07/mango-low-greenline-20220508-072600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/133/10/mango-low-greenline-20220513-104600.hdf5', 'Y'],
    #['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/135/10/mango-low-greenline-20220515-104400.hdf5', 'Y'],
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
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/012/06/mango-low-greenline-20220112-060200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/296/02/mango-low-greenline-20221023-023200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/170/04/mango-low-greenline-20220619-045200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/010/02/mango-low-greenline-20220110-021000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/030/02/mango-low-greenline-20220130-022000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/081/03/mango-low-greenline-20220322-030400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/069/12/mango-low-greenline-20220310-120000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/067/07/mango-low-greenline-20220308-070000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/048/12/mango-low-greenline-20220217-122200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/051/04/mango-low-greenline-20220220-040600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/052/02/mango-low-greenline-20220221-024200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/116/09/mango-low-greenline-20220426-095600.hdf5', 'N'], #37

    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/054/10/mango-low-greenline-20220223-104000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/034/12/mango-low-greenline-20220203-122600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/032/10/mango-low-greenline-20220201-103200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/031/03/mango-low-greenline-20220131-032200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/028/02/mango-low-greenline-20220128-024200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/027/11/mango-low-greenline-20220127-112400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/022/03/mango-low-greenline-20220122-033400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/362/04/mango-low-greenline-20221228-040600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/346/10/mango-low-greenline-20221212-103600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/331/04/mango-low-greenline-20221127-043400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/328/03/mango-low-greenline-20221124-031400.hdf5', 'Y'],

    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/297/05/mango-blo-greenline-20221024-052400.hdf5', 'N'], #blo starts here need 4 N 1y
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/297/02/mango-blo-greenline-20221024-024400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/309/10/mango-blo-greenline-20221105-103200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/273/03/mango-blo-greenline-20220930-030000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/240/05/mango-blo-greenline-20220828-050000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/217/09/mango-blo-greenline-20220805-092600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/204/09/mango-blo-greenline-20220723-094000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/156/06/mango-blo-greenline-20220605-062400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/156/05/mango-blo-greenline-20220605-050600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/170/09/mango-blo-greenline-20220619-092000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/128/06/mango-blo-greenline-20220508-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/132/10/mango-blo-greenline-20220512-101200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/140/07/mango-blo-greenline-20220520-070400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/148/07/mango-blo-greenline-20220528-072600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/148/09/mango-blo-greenline-20220528-090600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/324/05/mango-blo-greenline-20221120-051600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/285/02/mango-blo-greenline-20221012-022400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/275/07/mango-blo-greenline-20221002-073000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/297/11/mango-blo-greenline-20221024-110000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/236/06/mango-blo-greenline-20220824-062600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/243/07/mango-blo-greenline-20220831-074000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/258/05/mango-blo-greenline-20220915-050000.hdf5', 'Y'], #70
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/264/06/mango-blo-greenline-20220921-062800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/262/08/mango-blo-greenline-20220919-083000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/250/08/mango-blo-greenline-20220907-080800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/246/05/mango-blo-greenline-20220903-053800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/293/07/mango-blo-greenline-20221020-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/100/10/mango-blo-greenline-20220410-101800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/305/05/mango-blo-greenline-20221101-050400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/291/04/mango-blo-greenline-20221018-043800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/292/05/mango-blo-greenline-20221019-051000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/298/08/mango-blo-greenline-20221025-082400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/299/02/mango-blo-greenline-20221026-023400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/299/05/mango-blo-greenline-20221026-055800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/288/04/mango-blo-greenline-20221015-040400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/277/05/mango-blo-greenline-20221004-054400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/268/08/mango-blo-greenline-20220925-083000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/271/07/mango-blo-greenline-20220928-073200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/233/07/mango-blo-greenline-20220821-073200.hdf5', 'Y'],
   # ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/188/08/mango-blo-greenline-20220707-083400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/185/07/mango-blo-greenline-20220704-072800.hdf5', 'Y'],

    #BDR Data
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/359/03/mango-bdr-greenline-20221225-031400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/359/06/mango-bdr-greenline-20221225-063800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/071/04/mango-bdr-greenline-20230312-040600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/071/03/mango-bdr-greenline-20230312-032200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/091/09/mango-bdr-greenline-20230401-094200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/073/02/mango-bdr-greenline-20230314-020800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/359/08/mango-bdr-greenline-20221225-081600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/017/04/mango-bdr-greenline-20230117-041000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/026/08/mango-bdr-greenline-20230126-084800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/151/09/mango-bdr-greenline-20230531-091200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/177/08/mango-bdr-greenline-20230626-085800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/166/07/mango-bdr-greenline-20230615-074200.hdf5', 'Y'],#100
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/121/09/mango-bdr-greenline-20230501-093400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/015/07/mango-bdr-greenline-20230115-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/042/03/mango-bdr-greenline-20230211-034400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/086/08/mango-bdr-greenline-20230327-080600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/028/03/mango-bdr-greenline-20230128-034000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/043/07/mango-bdr-greenline-20230212-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/048/05/mango-bdr-greenline-20230217-053800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/051/05/mango-bdr-greenline-20230220-054200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/059/07/mango-bdr-greenline-20230228-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/119/09/mango-bdr-greenline-20230429-094200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/107/04/mango-bdr-greenline-20230417-043800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/103/05/mango-bdr-greenline-20230413-053400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/070/03/mango-bdr-greenline-20230311-034200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/022/04/mango-bdr-greenline-20230122-044800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/004/11/mango-bdr-greenline-20230104-114000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/095/10/mango-bdr-greenline-20230405-103200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/105/06/mango-bdr-greenline-20230415-063600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/077/07/mango-bdr-greenline-20230318-073600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/077/11/mango-bdr-greenline-20230318-110000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/114/05/mango-bdr-greenline-20230424-053600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/028/09/mango-bdr-greenline-20230128-094200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/045/04/mango-bdr-greenline-20230214-043400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/113/07/mango-bdr-greenline-20230423-073400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/102/06/mango-bdr-greenline-20230412-061000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/347/05/mango-bdr-greenline-20221213-051200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/082/05/mango-bdr-greenline-20230323-052200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/076/06/mango-bdr-greenline-20230317-061600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/132/05/mango-bdr-greenline-20230512-054000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/141/10/mango-bdr-greenline-20230521-100000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/338/11/mango-bdr-greenline-20221204-113800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/089/08/mango-bdr-greenline-20230330-084800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/100/03/mango-bdr-greenline-20230410-031000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/002/08/mango-bdr-greenline-20230102-085400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/024/04/mango-bdr-greenline-20230124-045400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/127/02/mango-bdr-greenline-20230507-024800.hdf5', 'N'], 

#https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/095/10/ really cool hour of lightning

    #CFS DATA
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/105/09/mango-cfs-greenline-20230415-091200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/131/07/mango-cfs-greenline-20230511-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/131/09/mango-cfs-greenline-20230511-090600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/201/09/mango-cfs-greenline-20230720-091000.hdf5', 'Y'], #140
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/189/05/mango-cfs-greenline-20230708-053200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/113/08/mango-cfs-greenline-20230423-080400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/119/10/mango-cfs-greenline-20230429-103000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/111/06/mango-cfs-greenline-20230421-064200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/087/11/mango-cfs-greenline-20230328-110000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/101/06/mango-cfs-greenline-20230411-063800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/116/07/mango-cfs-greenline-20230426-073400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/109/08/mango-cfs-greenline-20230419-081800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/107/09/mango-cfs-greenline-20230417-094000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/143/08/mango-cfs-greenline-20230523-084800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/077/03/mango-cfs-greenline-20230318-032800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/103/05/mango-cfs-greenline-20230413-054200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/083/07/mango-cfs-greenline-20230324-075000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/085/06/mango-cfs-greenline-20230326-064000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/150/10/mango-cfs-greenline-20230530-100600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/178/06/mango-cfs-greenline-20230627-064000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/166/08/mango-cfs-greenline-20230615-080000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/058/07/mango-cfs-greenline-20230227-074600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/183/10/mango-cfs-greenline-20230702-100000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/195/08/mango-cfs-greenline-20230714-083000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/169/05/mango-cfs-greenline-20230618-053800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/190/07/mango-cfs-greenline-20230709-073200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/176/06/mango-cfs-greenline-20230625-062800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/180/10/mango-cfs-greenline-20230629-100400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/144/06/mango-cfs-greenline-20230524-060800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/170/07/mango-cfs-greenline-20230619-074400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/201/07/mango-cfs-greenline-20230720-074200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/192/07/mango-cfs-greenline-20230711-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/019/06/mango-cfs-greenline-20230119-063600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/021/04/mango-cfs-greenline-20230121-043600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/042/06/mango-cfs-greenline-20230211-064200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/023/10/mango-cfs-greenline-20230123-102800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/140/07/mango-cfs-greenline-20230520-073000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/140/08/mango-cfs-greenline-20230520-081000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/144/06/mango-cfs-greenline-20230524-065000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/171/08/mango-cfs-greenline-20230620-080000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/147/09/mango-cfs-greenline-20230527-095000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/195/06/mango-cfs-greenline-20230714-064000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/195/06/mango-cfs-greenline-20230714-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/133/08/mango-cfs-greenline-20230513-080000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/166/05/mango-cfs-greenline-20230615-053200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/166/10/mango-cfs-greenline-20230615-100400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/133/05/mango-cfs-greenline-20230513-053800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/070/05/mango-cfs-greenline-20230311-050000.hdf5', 'N'], #huge number of dead pixels
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/089/08/mango-cfs-greenline-20230330-085000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/108/08/mango-cfs-greenline-20230418-085200.hdf5', 'N'], #good example
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/108/05/mango-cfs-greenline-20230418-054000.hdf5', 'N'], #187
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/005/09/mango-cvo-redline-20240105-092400.hdf5', 'Y'], #CVO RedLine Start: 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/041/07/mango-cvo-redline-20240210-073200.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/089/04/mango-cvo-redline-20240329-040400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/097/05/mango-cvo-redline-20240406-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/134/08/mango-cvo-redline-20240513-082800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/148/07/mango-cvo-redline-20240527-071600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/335/02/mango-cvo-redline-20221201-021200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/346/06/mango-cvo-redline-20221212-060800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/113/06/mango-cvo-redline-20220423-060800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/113/08/mango-cvo-redline-20220423-081200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/139/08/mango-cvo-redline-20220519-080400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/144/07/mango-cvo-redline-20220524-071600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/148/09/mango-cvo-redline-20220528-090400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/155/09/mango-cvo-redline-20220604-091200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/185/08/mango-cvo-redline-20220704-082400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/180/09/mango-cvo-redline-20220629-091200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/272/06/mango-cvo-redline-20220929-060800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/281/12/mango-cvo-redline-20221008-123200.hdf5', 'Y'], #done with CVO clear images (need 7 more cloudy from this line)
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/295/05/mango-cvo-redline-20221022-050000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/299/04/mango-cvo-redline-20221026-040400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/316/02/mango-cvo-redline-20221112-022800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/327/02/mango-cvo-redline-20221123-022800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/333/07/mango-cvo-redline-20221129-074000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/335/02/mango-cvo-redline-20221201-022000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/360/04/mango-cvo-redline-20221226-043200.hdf5', 'N'],

    #Below this line are images added for publication (unify red-green algoritm)
    #Site CFS, Utah
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/246/03/mango-cfs-redline-20240902-032800.hdf5', 'N'], #Started Here Sept 8
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/244/07/mango-cfs-redline-20240831-074000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/236/04/mango-cfs-redline-20240823-041200.hdf5', 'N'], #don't remove this one, great cloudy example, check video footage
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/235/04/mango-cfs-redline-20240822-043600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/231/04/mango-cfs-redline-20240818-041600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/220/04/mango-cfs-redline-20240807-041200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/120/09/mango-cfs-redline-20240429-090800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/123/06/mango-cfs-redline-20240502-064400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/283/09/mango-cfs-redline-20231010-094400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/259/07/mango-cfs-redline-20230916-071200.hdf5', 'Y'], #35 red here

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/181/09/mango-cfs-redline-20230630-093600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/162/08/mango-cfs-redline-20230611-084800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/321/02/mango-cfs-redline-20221117-024000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/305/07/mango-cfs-redline-20221101-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/295/09/mango-cfs-redline-20221022-092400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/233/04/mango-cfs-redline-20220821-041600.hdf5', 'N'], #check clarity on this one
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/196/06/mango-cfs-redline-20220715-062400.hdf5', 'N'], #check clarity on this one
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/152/05/mango-cfs-redline-20220601-050400.hdf5', 'N'], #check clarity on this one
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/088/03/mango-cfs-redline-20220329-031600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/001/02/mango-cfs-redline-20220101-023200.hdf5', 'N'], #45 here and check quality (jan 01/2022 is image date) 

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/082/03/mango-cfs-redline-20220323-033200.hdf5', 'Y'], #Started here sept 9
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/364/05/mango-cfs-redline-20211230-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/334/05/mango-cfs-redline-20211130-052000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/299/04/mango-cfs-redline-20211026-045600.hdf5', 'N'], #this one has many visible stars, but if it isn't like 100% CLEAR, it isn't clear
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/275/08/mango-cfs-redline-20211002-080400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/243/09/mango-cfs-redline-20210831-091200.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/228/07/mango-cfs-redline-20210816-075200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/112/03/mango-cfs-redline-20230422-034400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/138/07/mango-cfs-redline-20230518-074800.hdf5', 'N'], #review this, 55 here

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/173/08/mango-cfs-redline-20230622-080800.hdf5', 'Y'], #Started here sept 10
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/204/09/mango-cfs-redline-20230723-092000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/252/07/mango-cfs-redline-20230909-071200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/316/06/mango-cfs-redline-20231112-065600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/351/07/mango-cfs-redline-20231217-072800.hdf5', 'Y'], #60 Here. Need more cloudy images
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/357/02/mango-cfs-redline-20231223-022400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/033/06/mango-cfs-redline-20240202-064800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/068/03/mango-cfs-redline-20240308-033200.hdf5', 'N'], #while the stars are still relatively clear, this is a good example of a median image, in which case we lean to N
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/253/06/mango-cfs-redline-20240909-061600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/118/05/mango-cfs-redline-20240427-051600.hdf5', 'N'], #Another median image. 65 here. Change site
    #Site PAR, North Carolina
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/205/03/mango-par-redline-20240723-035600.hdf5', 'N'], #Started here sept 12
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/157/02/mango-par-redline-20240605-024800.hdf5', 'N'], #light example
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/123/04/mango-par-redline-20240502-041200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/120/02/mango-par-redline-20240429-020800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/086/01/mango-par-redline-20240326-015200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/031/05/mango-par-redline-20240131-052800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/230/07/mango-par-redline-20230818-074800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/164/07/mango-par-redline-20230613-070400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/313/05/mango-par-redline-20231109-050000.hdf5', 'Y'], #Not great
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/343/06/mango-par-redline-20231209-060400.hdf5', 'Y'], #75 here

    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/364/02/mango-par-redline-20231230-021600.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2022/230/06/mango-par-redline-20220818-063200.hdf5', 'N'],
    #Site EIO, Iowa
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/249/02/mango-eio-redline-20220906-024000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/269/02/mango-eio-redline-20220926-020800.hdf5', 'Y'], #dirt on the lens. TBD what to do with this type of image. Issue is present with all images at this site
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/299/07/mango-eio-redline-20221026-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/326/05/mango-eio-redline-20221122-052000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/104/04/mango-eio-redline-20230414-042000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/169/06/mango-eio-redline-20230618-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/203/08/mango-eio-redline-20230722-084000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/237/03/mango-eio-redline-20230825-030800.hdf5', 'N'], #85 here. moon maybe present here? Review if it causes an issue. 
    #Site MTO, North Dakota
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/258/03/mango-mto-redline-20240914-033600.hdf5', 'N'], #Started here sept 14
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/222/05/mango-mto-redline-20240809-050800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/212/05/mango-mto-redline-20240730-052400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/165/07/mango-mto-redline-20240613-071200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/148/07/mango-mto-redline-20240527-072400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/100/05/mango-mto-redline-20240409-052000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/088/03/mango-mto-redline-20240328-034000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/032/04/mango-mto-redline-20240201-041200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/337/01/mango-mto-redline-20231203-014400.hdf5', 'Y'], #Is october 31 2023 an aurora? Didn't include, but check it out I guess
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/291/02/mango-mto-redline-20231018-020400.hdf5', 'N'], #95 here. Debatably cloudy, but bottom half was covered pretty well so I think it counts. If it isn't obviously clear, it's cloudy

    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/259/02/mango-mto-redline-20240915-023600.hdf5', 'N'] ,#Started here sept 15s
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/288/01/mango-mto-redline-20231015-014000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/258/04/mango-mto-redline-20230915-042000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/227/05/mango-mto-redline-20230815-054800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/196/06/mango-mto-redline-20230715-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/168/06/mango-mto-redline-20230617-061200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/102/05/mango-mto-redline-20230412-053200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/251/03/mango-mto-redline-20230908-034000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/206/05/mango-mto-redline-20230725-053200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/060/03/mango-mto-redline-20240229-032400.hdf5', 'Y'], #105 Here. 
    
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/243/06/mango-mto-redline-20240830-064000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/215/07/mango-mto-redline-20240802-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/198/06/mango-mto-redline-20240716-065600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/193/07/mango-mto-redline-20240711-074400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/188/07/mango-mto-redline-20240706-073200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/183/07/mango-mto-redline-20240701-071600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/174/06/mango-mto-redline-20240622-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/162/06/mango-mto-redline-20240610-064800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/156/07/mango-mto-redline-20240604-070800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/137/05/mango-mto-redline-20240516-052400.hdf5', 'N'], #115 Here.
    #Site PAR, North Carolina
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/150/04/mango-par-redline-20240529-040000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/181/05/mango-par-redline-20240629-052800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/193/08/mango-par-redline-20240711-080800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/242/03/mango-par-redline-20240829-032000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/253/01/mango-par-redline-20240909-013200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/017/05/mango-par-redline-20240117-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/012/03/mango-par-redline-20240112-030400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/005/03/mango-par-redline-20240105-033200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/337/00/mango-par-redline-20231203-003200.hdf5', 'N'], #Iffy
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/278/01/mango-par-redline-20231005-010800.hdf5', 'N'] #125 Here.














    ]

    return urls