import ast
objParam = {}
objParam["0001"]="AD"
objParam["0002"]="7B"
objParam["0003"]="49"
objParam["0004"]="17"
objParam["0005"]="E5"
objParam["0006"]="B3"
objParam["0007"]="81"
objParam["0008"]="4F"
objParam["0009"]="1D"
objParam["0010"]="8C"
objParam["0011"]="5A"
objParam["0012"]="28"
objParam["0101"]="39"
objParam["0102"]="07"
objParam["0103"]="D5"
objParam["0104"]="A3"
objParam["0105"]="71"
objParam["0106"]="3F"
objParam["0107"]="0D"
objParam["0108"]="DB"
objParam["0109"]="A9"
objParam["0110"]="18"
objParam["0111"]="E6"
objParam["0112"]="B4"
objParam["0201"]="C5"
objParam["0202"]="93"
objParam["0203"]="61"
objParam["0204"]="2F"
objParam["0205"]="FD"
objParam["0206"]="CB"
objParam["0207"]="99"
objParam["0208"]="67"
objParam["0209"]="35"
objParam["0210"]="A4"
objParam["0211"]="72"
objParam["0212"]="40"
objParam["0301"]="51"
objParam["0302"]="1F"
objParam["0303"]="ED"
objParam["0304"]="BB"
objParam["0305"]="89"
objParam["0306"]="57"
objParam["0307"]="25"
objParam["0308"]="F3"
objParam["0309"]="C1"
objParam["0310"]="30"
objParam["0311"]="FE"
objParam["0312"]="CC"
objParam["0401"]="DD"
objParam["0402"]="AB"
objParam["0403"]="79"
objParam["0404"]="47"
objParam["0405"]="15"
objParam["0406"]="E3"
objParam["0407"]="B1"
objParam["0408"]="7F"
objParam["0409"]="4D"
objParam["0410"]="BC"
objParam["0411"]="8A"
objParam["0412"]="58"
objParam["0501"]="69"
objParam["0502"]="37"
objParam["0503"]="05"
objParam["0504"]="D3"
objParam["0505"]="A1"
objParam["0506"]="6F"
objParam["0507"]="3D"
objParam["0508"]="0B"
objParam["0509"]="D9"
objParam["0510"]="48"
objParam["0511"]="16"
objParam["0512"]="E4"
objParam["0601"]="F5"
objParam["0602"]="C3"
objParam["0603"]="91"
objParam["0604"]="5F"
objParam["0605"]="2D"
objParam["0606"]="FB"
objParam["0607"]="C9"
objParam["0608"]="97"
objParam["0609"]="65"
objParam["0610"]="D4"
objParam["0611"]="A2"
objParam["0612"]="70"
objParam["0701"]="81"
objParam["0702"]="4F"
objParam["0703"]="1D"
objParam["0704"]="EB"
objParam["0705"]="B9"
objParam["0706"]="87"
objParam["0707"]="55"
objParam["0708"]="23"
objParam["0709"]="F1"
objParam["0710"]="60"
objParam["0711"]="2E"
objParam["0712"]="FC"
objParam["0801"]="0D"
objParam["0802"]="DB"
objParam["0803"]="A9"
objParam["0804"]="77"
objParam["0805"]="45"
objParam["0806"]="13"
objParam["0807"]="E1"
objParam["0808"]="AF"
objParam["0809"]="7D"
objParam["0810"]="EC"
objParam["0811"]="BA"
objParam["0812"]="88"
objParam["0901"]="99"
objParam["0902"]="67"
objParam["0903"]="35"
objParam["0904"]="03"
objParam["0905"]="D1"
objParam["0906"]="9F"
objParam["0907"]="6D"
objParam["0908"]="3B"
objParam["0909"]="09"
objParam["0910"]="78"
objParam["0911"]="46"
objParam["0912"]="14"
objParam["1001"]="18"
objParam["1002"]="E6"
objParam["1003"]="B4"
objParam["1004"]="82"
objParam["1005"]="50"
objParam["1006"]="1E"
objParam["1007"]="EC"
objParam["1008"]="BA"
objParam["1009"]="88"
objParam["1010"]="F7"
objParam["1011"]="C5"
objParam["1012"]="93"
objParam["1101"]="A4"
objParam["1102"]="72"
objParam["1103"]="40"
objParam["1104"]="0E"
objParam["1105"]="DC"
objParam["1106"]="AA"
objParam["1107"]="78"
objParam["1108"]="46"
objParam["1109"]="14"
objParam["1110"]="83"
objParam["1111"]="51"
objParam["1112"]="1F"
objParam["1201"]="30"
objParam["1202"]="FE"
objParam["1203"]="CC"
objParam["1204"]="9A"
objParam["1205"]="68"
objParam["1206"]="36"
objParam["1207"]="04"
objParam["1208"]="D2"
objParam["1209"]="A0"
objParam["1210"]="0F"
objParam["1211"]="DD"
objParam["1212"]="AB"
objParam["1301"]="BC"
objParam["1302"]="8A"
objParam["1303"]="58"
objParam["1304"]="26"
objParam["1305"]="F4"
objParam["1306"]="C2"
objParam["1307"]="90"
objParam["1308"]="5E"
objParam["1309"]="2C"
objParam["1310"]="9B"
objParam["1311"]="69"
objParam["1312"]="37"
objParam["1401"]="48"
objParam["1402"]="16"
objParam["1403"]="E4"
objParam["1404"]="B2"
objParam["1405"]="80"
objParam["1406"]="4E"
objParam["1407"]="1C"
objParam["1408"]="EA"
objParam["1409"]="B8"
objParam["1410"]="27"
objParam["1411"]="F5"
objParam["1412"]="C3"
objParam["1501"]="D4"
objParam["1502"]="A2"
objParam["1503"]="70"
objParam["1504"]="3E"
objParam["1505"]="0C"
objParam["1506"]="DA"
objParam["1507"]="A8"
objParam["1508"]="76"
objParam["1509"]="44"
objParam["1510"]="B3"
objParam["1511"]="81"
objParam["1512"]="4F"
objParam["1601"]="60"
objParam["1602"]="2E"
objParam["1603"]="FC"
objParam["1604"]="CA"
objParam["1605"]="98"
objParam["1606"]="66"
objParam["1607"]="34"
objParam["1608"]="02"
objParam["1609"]="D0"
objParam["1610"]="3F"
objParam["1611"]="0D"
objParam["1612"]="DB"
objParam["1701"]="EC"
objParam["1702"]="BA"
objParam["1703"]="88"
objParam["1704"]="56"
objParam["1705"]="24"
objParam["1706"]="F2"
objParam["1707"]="C0"
objParam["1708"]="8E"
objParam["1709"]="5C"
objParam["1710"]="CB"
objParam["1711"]="99"
objParam["1712"]="67"
objParam["1801"]="78"
objParam["1802"]="5F"
objParam["1803"]="2D"
objParam["1804"]="FB"
objParam["1805"]="C9"
objParam["1806"]="97"
objParam["1807"]="65"
objParam["1808"]="33"
objParam["1809"]="01"
objParam["1810"]="70"
objParam["1811"]="3E"
objParam["1812"]="0C"


for param in objParam:
  print(param)
  

def parser_race_params_get_cname(yyyymm):
  return str(yyyymm)

