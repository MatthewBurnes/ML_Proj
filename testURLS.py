def getURL():
    urls = [['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/010/03/mango-mro-greenline-20230110-030000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/116/05/mango-mro-greenline-20230426-054400.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/116/10/mango-mro-greenline-20230426-105200.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/091/11/mango-mro-greenline-20230401-111400.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/121/10/mango-mro-greenline-20230501-101000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/322/06/mango-mro-greenline-20231118-060000.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/320/06/mango-mro-greenline-20231116-060200.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/312/05/mango-mro-greenline-20231108-051800.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/307/03/mango-mro-greenline-20231103-030000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/270/11/mango-mro-greenline-20230927-110400.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/285/09/mango-mro-greenline-20231012-091000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2022/325/10/mango-mro-greenline-20221121-101000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2022/352/07/mango-mro-greenline-20221218-072000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2022/352/12/mango-mro-greenline-20221218-121200.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2022/344/01/mango-mro-greenline-20221210-013000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2022/365/08/mango-mro-greenline-20221231-081600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2022/357/04/mango-mro-greenline-20221223-041200.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/117/10/mango-mro-greenline-20230427-100400.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/136/06/mango-mro-greenline-20230516-061800.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/119/09/mango-mro-greenline-20230429-090800.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/262/07/mango-mro-greenline-20230919-071800.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/131/04/mango-mro-greenline-20230511-041400.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/246/03/mango-mro-greenline-20230903-030000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/290/02/mango-mro-greenline-20231017-021800.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/290/11/mango-mro-greenline-20231017-110600.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/074/03/mango-mro-greenline-20230315-032600.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/057/10/mango-mro-greenline-20230226-102200.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/100/03/mango-mro-greenline-20230410-032000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/087/08/mango-mro-greenline-20230328-081000.hdf5', 'Y'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/085/05/mango-mro-greenline-20230326-050800.hdf5', 'Y'],  #25 clear, 25 cloudy
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/264/06/mango-mro-greenline-20230921-064200.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/266/05/mango-mro-greenline-20230923-055600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/282/02/mango-mro-greenline-20231009-021000.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/283/04/mango-mro-greenline-20231010-041600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/297/08/mango-mro-greenline-20231024-083800.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/298/03/mango-mro-greenline-20231025-034400.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/313/07/mango-mro-greenline-20231109-074600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/313/12/mango-mro-greenline-20231109-120800.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/319/10/mango-mro-greenline-20231115-105400.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/320/08/mango-mro-greenline-20231116-083000.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/321/01/mango-mro-greenline-20231117-013400.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/322/03/mango-mro-greenline-20231118-031000.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/122/10/mango-mro-greenline-20230502-100201.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/124/09/mango-mro-greenline-20230504-093200.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/133/03/mango-mro-greenline-20230513-033800.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/135/05/mango-mro-greenline-20230515-052600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/135/05/mango-mro-greenline-20230515-053000.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/229/06/mango-mro-greenline-20230817-063600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/231/05/mango-mro-greenline-20230819-053600.hdf5', 'N'],
            ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/233/03/mango-mro-greenline-20230821-032000.hdf5', 'N']
            ]
    return urls
