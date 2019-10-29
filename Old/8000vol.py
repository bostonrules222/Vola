import csv
import quandl
import numpy as np
import pandas as pd
import sys

from statistics import mean 
from statistics import median
quandl.ApiConfig.api_key = '-Kiku-Vx2R6nNT7svt4D'
medians = []
averages = []

codelist = ['A','AA','AAC','AAL','AAN','AAOI','AAON','AAP','AAPL','AAT','AAU','AAWW','AAXJ','AAXN','AB','ABB','ABBV','ABC','ABCB','ABDC','ABEO','ABEV','ABG','ABM','ABMD','ABR','ABT','ABTX','ABUS','ACA','ACAD','ACB','ACC','ACCO','ACGL','ACH','ACHC','ACHN','ACIA','ACIW','ACLS','ACM','ACN','ACOR','ACRE','ACRS','ACRX','ACTG','ACWI','ACWX','ADAP','ADBE','ADC','ADI','ADM','ADMA','ADMP','ADMS','ADNT','ADP','ADPT','ADRO','ADS','ADSK','ADSW','ADT','ADTN','ADUS','ADVM','AEE','AEG','AEGN','AEIS','AEL','AEM','AEO','AEP','AER','AERI','AES','AEZS','AFG','AFH','AFI','AFL','AFMD','AFTY','AFYA','AG','AGCO','AGEN','AGFS','AGG','AGI','AGIO','AGLE','AGM','AGN','AGNC','AGO','AGQ','AGR','AGRO','AGRX','AGS','AGTC','AGX','AGYS','AHC','AHH','AHT','AI','AIA','AIG','AIMC','AIMT','AIN','AINV','AIR','AIRG','AIT','AIV','AIZ','AJG','AJRD','AKAM','AKBA','AKCA','AKG','AKR','AKRX','AKS','AKTS','AL','ALB','ALBO','ALC','ALDX','ALE','ALEX','ALG','ALGN','ALGT','ALIM','ALK','ALKS','ALL','ALLE','ALLK','ALLO','ALLT','ALLY','ALNY','ALRM','ALSK','ALSN','ALT','ALTM','ALTR','ALV','ALXN','AM','AMAG','AMAT','AMBA','AMBC','AMC','AMCR','AMCX','AMD','AME','AMED','AMG','AMGN','AMH','AMJ','AMKR','AMLP','AMN','AMNB','AMOT','AMP','AMPE','AMPH','AMPY','AMRC','AMRN','AMRS','AMRX','AMSC','AMSF','AMSWA','AMT','AMTD','AMWD','AMX','AMZA','AMZN','AN','ANAB','ANAT','ANDE','ANET','ANF','ANFI','ANGI','ANGL','ANGO','ANH','ANIK','ANIP','ANSS','ANTE','ANTM','AOBC','AON','AOS','AOSL','AP','APA','APAM','APD','APDN','APEI','APEX','APH','APHA','APLE','APLS','APO','APOG','APPF','APPN','APPS','APRN','APT','APTO','APTS','APTV','APVO','APY','APYX','AQMS','AQUA','AR','ARA','ARAV','ARAY','ARC','ARCB','ARCC','ARCH','ARCO','ARCT','ARD','ARDX','ARE','ARES','AREX','ARGT','ARGX','ARI','ARKK','ARKW','ARLO','ARLP','ARMK','ARNA','ARNC','AROC','AROW','ARQL','ARR','ARTNA','ARTX','ARVN','ARW','ARWR','ASA','ASB','ASC','ASFI','ASGN','ASH','ASHR','ASHS','ASIX','ASMB','ASML','ASNA','ASND','ASPS','ASR','ASRT','ASRV','ASTE','ASUR','ASYS','AT','ATAX','ATEC','ATEN','ATEX','ATGE','ATH','ATHM','ATHX','ATI','ATKR','ATLC','ATNI','ATNM','ATNX','ATO','ATOS','ATR','ATRA','ATRC','ATRS','ATSG','ATUS','ATVI','AU','AUB','AUDC','AUMN','AUPH','AUTO','AUY','AVA','AVAV','AVB','AVD','AVDL','AVEO','AVGO','AVH','AVID','AVLR','AVNS','AVP','AVRO','AVT','AVTR','AVX','AVXL','AVY','AVYA','AWI','AWK','AWR','AWRE','AX','AXAS','AXDX','AXE','AXGN','AXGT','AXL','AXNX','AXP','AXS','AXSM','AXTA','AXTI','AXU','AY','AYI','AYR','AYX','AZN','AZO','AZPN','AZUL','AZZ','B','BA','BABA','BAC','BAH','BAL','BAM','BANC','BAND','BANR','BAP','BAS','BATRA','BATRK','BAX','BB','BBAR','BBBY','BBD','BBDC','BBH','BBL','BBSI','BBT','BBU','BBVA','BBW','BBY','BC','BCBP','BCC','BCE','BCEI','BCI','BCLI','BCO','BCOR','BCOV','BCPC','BCRX','BCS','BCSF','BDC','BDGE','BDN','BDSI','BDX','BE','BEAT','BECN','BELFB','BEN','BERY','BEST','BF_A','BFAM','BF_B','BFOR','BG','BGCP','BGFV','BGG','BGNE','BGS','BHC','BHE','BHF','BHLB','BHP','BHR','BHVN','BIB','BIDU','BIG','BIIB','BIL','BILI','BIO','BIOS','BIP','BIS','BITA','BIV','BJ','BJK','BJRI','BK','BKCC','BKD','BKE','BKEP','BKF','BKH','BKI','BKLN','BKNG','BKR','BKU','BL','BLCM','BLCN','BLD','BLDP','BLDR','BLFS','BLK','BLKB','BLL','BLMN','BLNK','BLOK','BLUE','BLV','BLX','BMA','BMCH','BMI','BMLP','BMO','BMRN','BMTC','BMY','BND','BNDX','BNED','BNFT','BNO','BNS','BOCH','BOH','BOIL','BOKF','BOLD','BOND','BOOM','BOOT','BOTZ','BOX','BP','BPFH','BPL','BPMC','BPMP','BPOP','BPR','BPT','BPY','BR','BRC','BREW','BRF','BRFS','BRG','BRK_B','BRKL','BRKR','BRKS','BRO','BRX','BRY','BRZU','BSAC','BSBR','BSET','BSGM','BSM','BSMX','BSQR','BSRR','BSV','BSX','BTE','BTG','BTI','BTN','BTU','BUD','BURL','BUSE','BV','BVN','BW','BWA','BWX','BWXT','BX','BXC','BXMT','BXP','BXS','BYD','BYND','BZH','BZQ','BZUN','C','CAAS','CAC','CACC','CACI','CADE','CAE','CAF','CAG','CAH','CAI','CAJ','CAKE','CAL','CALA','CALM','CALX','CAMP','CAMT','CANE','CAPL','CAR','CARA','CARB','CARG','CARS','CASA','CASH','CASS','CASY','CAT','CATB','CATM','CATO','CATS','CATY','CB','CBAY','CBB','CBD','CBIO','CBL','CBM','CBMG','CBPO','CBPX','CBRE','CBRL','CBS','CBS_A','CBSH','CBT','CBU','CBZ','CC','CCC','CCEP','CCI','CCJ','CCK','CCL','CCLP','CCMP','CCNE','CCO','CCOI','CCRN','CCS','CCXI','CDAY','CDE','CDEV','CDK','CDLX','CDMO','CDNA','CDNS','CDR','CDTX','CDW','CDXC','CDXS','CDZI','CE','CECE','CECO','CEIX','CEL','CELG','CELH','CENT','CENTA','CENX','CEO','CEQP','CERC','CERN','CERS','CETV','CEVA','CEW','CF','CFA','CFFN','CFG','CFR','CFX','CG','CGBD','CGC','CGEN','CGIX','CGNX','CHAD','CHAP','CHAU','CHCO','CHD','CHDN','CHE','CHEF','CHGG','CHH','CHIC','CHIQ','CHIX','CHK','CHKP','CHKR','CHL','CHMA','CHNG','CHRS','CHRW','CHS','CHT','CHTR','CHU','CHUY','CHWY','CI','CIA','CIB','CIBR','CIEN','CIG','CIM','CINF','CIO','CIR','CISN','CIT','CIVB','CJ','CKH','CL','CLAR','CLB','CLBK','CLBS','CLCT','CLDR','CLDT','CLDX','CLF','CLFD','CLGX','CLH','CLI','CLIR','CLLS','CLMT','CLNE','CLNY','CLR','CLS','CLSD','CLSN','CLUB','CLVS','CLW','CLX','CM','CMA','CMC','CMCM','CMCO','CMCSA','CMD','CME','CMG','CMI','CMO','CMP','CMPR','CMRE','CMRX','CMS','CMTL','CNA','CNAT','CNC','CNCE','CNDT','CNET','CNHI','CNI','CNK','CNMD','CNNE','CNO','CNOB','CNP','CNQ','CNR','CNS','CNSL','CNTY','CNX','CNXM','CNXN','CNXT','CO','CODI','COF','COG','COHR','COHU','COLB','COLL','COLM','COMM','CONE','CONN','COO','COOP','COP','COR','CORE','CORN','CORR','CORT','CORV','COST','COT','COTY','COUP','COW','COWN','CP','CPA','CPB','CPE','CPF','CPG','CPK','CPL','CPLG','CPLP','CPRI','CPRT','CPRX','CPS','CPSI','CPSS','CPT','CPTA','CQP','CR','CRAI','CRBP','CRC','CRCM','CRD_A','CREE','CRESY','CRH','CRI','CRIS','CRK','CRL','CRM','CRMD','CRMT','CRNC','CRNT','CROC','CRON','CROP','CROX','CRR','CRS','CRSP','CRTO','CRUS','CRVL','CRVS','CRWD','CRWS','CRY','CRZO','CS','CSCO','CSD','CSFL','CSGP','CSGS','CSII','CSIQ','CSL','CSLT','CSOD','CSTE','CSTM','CSU','CSV','CSWC','CSX','CTAS','CTB','CTBI','CTG','CTIC','CTL','CTLT','CTMX','CTRA','CTRC','CTRE','CTRN','CTRP','CTS','CTSH','CTSO','CTST','CTT','CTVA','CTXS','CUB','CUBE','CUBI','CUI','CUK','CULP','CURE','CURO','CUTR','CUZ','CVA','CVBF','CVCO','CVCY','CVE','CVEO','CVET','CVGI','CVGW','CVI','CVIA','CVLT','CVM','CVNA','CVS','CVTI','CVX','CVY','CW','CWB','CWCO','CWEB','CWEN','CWEN_A','CWH','CWI','CWK','CWST','CWT','CX','CXDC','CXO','CXP','CXW','CY','CYB','CYBR','CYD','CYH','CYOU','CYRN','CYRX','CYTK','CZNC','CZR','CZZ','D','DAKT','DAL','DAN','DAR','DB','DBA','DBB','DBC','DBD','DBE','DBEF','DBEU','DBI','DBJP','DBO','DBP','DBS','DBV','DBVT','DBX','DCI','DCO','DCOM','DCP','DCPH','DD','DDD','DDG','DDM','DDOG','DDS','DE','DEA','DECK','DEI','DELL','DEM','DENN','DEO','DERM','DES','DESP','DF','DFE','DFEN','DFIN','DFJ','DFS','DG','DGICA','DGII','DGL','DGLY','DGRO','DGRW','DGS','DGX','DHI','DHR','DHT','DHX','DIA','DIG','DIN','DIOD','DIS','DISCA','DISCK','DISH','DJP','DK','DKL','DKS','DL','DLB','DLN','DLNG','DLPH','DLR','DLS','DLTH','DLTR','DLX','DMLP','DMRC','DNKN','DNLI','DNN','DNOW','DNR','DO','DOC','DOCU','DOG','DOMO','DON','DOOR','DORM','DOV','DOVA','DOW','DOX','DOYU','DPK','DPLO','DPZ','DQ','DRD','DRE','DRH','DRI','DRIP','DRN','DRNA','DRQ','DRRX','DRV','DS','DSKE','DSL','DSPG','DSS','DSX','DT','DTE','DTEA','DTN','DUG','DUK','DUST','DVA','DVAX','DVN','DVY','DWAS','DWSN','DWX','DX','DXC','DXCM','DXD','DXJ','DXJS','DXLG','DXPE','DXYN','DY','DYAI','E','EA','EAF','EAT','EB','EBAY','EBF','EBIX','EBND','EBS','EBSB','EC','ECA','ECHO','ECL','ECNS','ECOL','ECOM','ECON','ECPG','ED','EDAP','EDC','EDIT','EDIV','EDU','EDZ','EE','EEB','EEFT','EEM','EET','EEV','EEX','EFA','EFC','EFOI','EFSC','EFU','EFX','EFZ','EGAN','EGBN','EGHT','EGLE','EGO','EGOV','EGP','EGRX','EGY','EHC','EHTH','EIDO','EIDX','EIG','EIGI','EIGR','EIX','EL','ELAN','ELD','ELF','ELGX','ELOX','ELP','ELS','ELY','EMAN','EMB','EME','EMKR','EMLC','EMLP','EMN','EMR','ENB','ENBL','ENDP','ENG','ENIA','ENIC','ENLC','ENPH','ENR','ENS','ENSG','ENT','ENTA','ENTG','ENV','ENVA','ENZ','ENZL','EOG','EOLS','EPAC','EPAM','EPAY','EPC','EPD','EPI','EPM','EPP','EPR','EPRT','EPV','EPZM','EQC','EQH','EQIX','EQM','EQNR','EQR','EQT','ERA','ERF','ERI','ERIC','ERIE','ERII','ERJ','EROS','ERUS','ERX','ERY','ES','ESCA','ESE','ESI','ESNT','ESPR','ESRT','ESS','ESTC','ET','ETFC','ETH','ETM','ETN','ETR','ETRN','ETSY','EUFN','EUM','EUO','EURL','EURN','EV','EVA','EVBG','EVC','EVFM','EVH','EVOP','EVR','EVRG','EVRI','EVTC','EW','EWA','EWBC','EWC','EWD','EWG','EWH','EWI','EWJ','EWK','EWL','EWM','EWN','EWP','EWQ','EWS','EWT','EWU','EWV','EWW','EWX','EWY','EWZ','EXAS','EXC','EXEL','EXK','EXLS','EXP','EXPD','EXPE','EXPO','EXPR','EXR','EXTN','EXTR','EYE','EYES','EYPT','EZA','EZJ','EZPW','F','FAF','FANG','FANH','FARO','FAS','FAST','FATE','FAZ','FB','FBC','FBHS','FBIZ','FBM','FBNC','FBP','FBT','FC','FCA','FCAU','FCBC','FCEL','FCF','FCFS','FCG','FCN','FCPT','FCX','FDIS','FDL','FDN','FDP','FDS','FDUS','FDX','FE','FELE','FELP','FEM','FENC','FENG','FENY','FEP','FET','FEX','FEYE','FEZ','FF','FFBC','FFG','FFIC','FFIN','FFIV','FFNW','FFTY','FG','FGEN','FGP','FHB','FHLC','FHN','FI','FIBK','FICO','FIDU','FII','FIS','FISI','FISV','FIT','FITB','FIVE','FIVN','FIW','FIX','FIXX','FIZZ','FL','FLDM','FLEX','FLIC','FLIR','FLNT','FLO','FLOW','FLR','FLS','FLT','FLWS','FLXN','FLY','FM','FMAT','FMBI','FMC','FMNB','FMS','FMX','FN','FNB','FNCL','FND','FNDA','FNDE','FNDF','FNDX','FNF','FNHC','FNJN','FNKO','FNLC','FNV','FOCS','FOE','FOLD','FOMX','FOR','FORM','FORR','FOSL','FOX','FOXA','FOXF','FPE','FPI','FPRX','FR','FRAC','FRAK','FRBK','FRC','FRGI','FRI','FRME','FRO','FRPT','FRT','FRTA','FSB','FSCT','FSK','FSLR','FSLY','FSM','FSP','FSS','FSTR','FTAG','FTAI','FTC','FTCH','FTDR','FTEC','FTEK','FTGC','FTI','FTK','FTNT','FTR','FTRI','FTS','FTSI','FTSV','FTV','FUL','FULT','FUN','FV','FVD','FWONA','FWONK','FWRD','FXA','FXB','FXC','FXD','FXE','FXF','FXG','FXH','FXI','FXL','FXN','FXO','FXP','FXR','FXS','FXU','FXY','FXZ','G','GABC','GAIN','GALT','GARS','GASL','GASS','GASX','GATX','GBCI','GBDC','GBT','GBX','GCAP','GCI','GCO','GCP','GD','GDDY','GDEN','GDI','GDOT','GDS','GDX','GDXJ','GE','GEF','GEL','GEM','GEMP','GEN','GEO','GEOS','GERN','GES','GFF','GFI','GFN','GGAL','GGB','GGG','GH','GHDX','GHL','GHM','GHYB','GIB','GIFI','GIGB','GIII','GIL','GILD','GILT','GIS','GKOS','GL','GLAD','GLD','GLDD','GLIBA','GLL','GLMD','GLNG','GLOB','GLOG','GLOP','GLP','GLPG','GLPI','GLRE','GLT','GLUU','GLW','GLYC','GM','GMAB','GME','GMED','GMF','GMLP','GMRE','GMS','GNC','GNCA','GNE','GNK','GNL','GNMK','GNMX','GNR','GNRC','GNSS','GNTX','GNW','GO','GOEX','GOGL','GOGO','GOL','GOLD','GOLF','GOOD','GOOG','GOOGL','GOOS','GORO','GOSS','GPC','GPI','GPK','GPL','GPMT','GPN','GPOR','GPRE','GPRK','GPRO','GPS','GPX','GRA','GRBK','GRC','GREK','GRFS','GRMN','GROW','GRPN','GRUB','GS','GSAT','GSB','GSBC','GSG','GSHD','GSIE','GSIT','GSK','GSKY','GSLC','GSM','GSS','GSUM','GSX','GT','GTE','GTES','GTHX','GTIM','GTLS','GTN','GTS','GTT','GTX','GTY','GUNR','GURE','GURU','GUSH','GV','GVA','GVIP','GWB','GWPH','GWR','GWRE','GWW','GWX','GXC','GXG','GYLD','H','HA','HABT','HACK','HAE','HAFC','HAIN','HAL','HALL','HALO','HAO','HAS','HASI','HAYN','HBAN','HBI','HBIO','HBM','HBNC','HBP','HCA','HCAT','HCC','HCCI','HCFT','HCHC','HCI','HCKT','HCP','HCR','HCSG','HD','HDB','HDGE','HDS','HDSN','HDV','HE','HEAR','HEDJ','HEES','HEI','HEI_A','HELE','HEP','HES','HESM','HEWG','HEWJ','HEXO','HEZU','HFC','HFWA','HGV','HHC','HI','HIBB','HIG','HII','HIIQ','HIL','HIMX','HIW','HL','HLF','HLI','HLIO','HLIT','HLNE','HLT','HLX','HMC','HMHC','HMI','HMN','HMST','HMSY','HMTV','HMY','HNGR','HNI','HNP','HNRG','HOFT','HOG','HOLI','HOLX','HOMB','HOME','HON','HOPE','HOS','HP','HPE','HPJ','HPP','HPQ','HPR','HQY','HR','HRB','HRC','HRI','HRL','HROW','HRTG','HRTX','HRZN','HSBC','HSC','HSIC','HSII','HST','HSTM','HSY','HT','HTA','HTBI','HTBK','HTGC','HTGM','HTH','HTHT','HTLD','HTLF','HTZ','HUBB','HUBG','HUBS','HUD','HUM','HUN','HURN','HUSA','HUYA','HVT','HWC','HWCC','HWKN','HXL','HY','HYG','HYGH','HYLB']
codelist2 = ['HYLD','HYMB','HYRE','HYS','HZN','HZNP','HZO','I','IAA','IAC','IAG','IAI','IART','IAT','IAU','IBB','IBCP','IBKC','IBKR','IBM','IBN','IBOC','IBP','IBTX','ICAD','ICD','ICE','ICFI','ICHR','ICLK','ICLR','ICMB','ICON','ICPT','ICUI','IDA','IDCC','IDEX','IDN','IDNA','IDRA','IDT','IDU','IDXX','IEF','IEI','IEMG','IEP','IEUR','IEV','IEX','IEZ','IFF','IFGL','IFN','IGC','IGF','IGIB','IGLB','IGM','IGN','IGOV','IGSB','IGT','IHAK','IHDG','IHE','IHF','IHI','IHY','IIIN','IIIV','IIN','IIPR','IIVI','IJH','IJJ','IJK','IJR','IJS','IJT','ILF','ILMN','ILPT','IMAX','IMGN','IMH','IMKTA','IMMR','IMMU','IMO','IMOS','INAP','INCY','INDB','INDL','INDY','INFI','INFN','INFO','INFY','ING','INGN','INGR','INN','INNT','INO','INOD','INOV','INSG','INSM','INSP','INST','INT','INTC','INTF','INTL','INTU','INVA','INVE','INVH','INWK','INXN','IO','IONS','IOO','IOSP','IOVA','IP','IPAR','IPAY','IPG','IPGP','IPHI','IPHS','IPI','IPO','IPOA','IQ','IQDF','IQV','IR','IRBO','IRBT','IRDM','IRET','IRM','IRT','IRTC','IRWD','ISBC','ISEE','ISIG','ISRA','ISRG','IT','ITCI','ITGR','ITI','ITOT','ITP','ITRI','ITT','ITUB','ITW','IUSG','IUSV','IVAC','IVC','IVE','IVR','IVV','IVW','IVZ','IWB','IWC','IWD','IWF','IWM','IWN','IWO','IWP','IWR','IWS','IWV','IXC','IXJ','IXN','IXP','IXUS','IYE','IYF','IYG','IYH','IYM','IYR','IYW','JACK','JAG','JAX','JAZZ','JBGS','JBHT','JBL','JBLU','JBSS','JBT','JCI','JCOM','JCP','JD','JDST','JE','JEC','JEF','JELD','JETS','JHG','JILL','JJC','JJG','JKHY','JKS','JLL','JMEI','JMIA','JNCE','JNJ','JNK','JNPR','JNUG','JO','JOBS','JOE','JP','JPEM','JPIN','JPM','JPNL','JPUS','JRJC','JUST','JW_A','JWN','JYNT','K','KAI','KALA','KALU','KAMN','KAR','KB','KBA','KBAL','KBE','KBH','KBR','KBWB','KCE','KDMN','KDP','KE','KEG','KELYA','KEM','KEP','KEX','KEY','KEYS','KFRC','KFY','KGC','KHC','KIDS','KIE','KIM','KIN','KIRK','KKR','KL','KLAC','KLIC','KLXE','KMB','KMI','KMPH','KMPR','KMT','KMX','KN','KNDI','KNL','KNOP','KNSL','KNX','KO','KODK','KOF','KOL','KOLD','KOP','KOPN','KOS','KPTI','KR','KRA','KRC','KRE','KRG','KRNT','KRNY','KRO','KSA','KSS','KSU','KT','KTB','KTCC','KTOS','KURA','KVHI','KW','KWEB','KWR','KYN','L','LABD','LABU','LAD','LADR','LAKE','LAMR','LANC','LAND','LASR','LAUR','LAZ','LB','LBAI','LBJ','LBRDA','LBRDK','LBRT','LBTYA','LBTYK','LBY','LC','LCI','LCII','LCNB','LCTX','LCUT','LDL','LDOS','LE','LEA','LEAF','LECO','LEE','LEG','LEJU','LEMB','LEN','LEVI','LFC','LFUS','LFVN','LGF_A','LGF_B','LGIH','LGND','LH','LHCG','LHX','LII','LILA','LILAK','LIN','LINC','LIT','LITE','LIVN','LJPC','LK','LKFN','LKQ','LKSD','LL','LLEX','LLNW','LLY','LM','LMAT','LMNR','LMNX','LMRK','LMT','LN','LNC','LNDC','LNG','LNN','LNT','LNTH','LOB','LOCO','LODE','LOGI','LOGM','LOMA','LONE','LOOP','LOPE','LORL','LOVE','LOW','LPCN','LPG','LPI','LPL','LPLA','LPSN','LPT','LPX','LQD','LQDH','LQDT','LRCX','LRGF','LRN','LSCC','LSI','LSTR','LSXMA','LTC','LTHM','LTM','LTPZ','LTRPA','LTXB','LULU','LUV','LVGO','LVS','LW','LX','LXFR','LXP','LXRX','LXU','LYB','LYFT','LYG','LYTS','LYV','LZB','M','MA','MAA','MAC','MACK','MAG','MAGS','MAIN','MAN','MANH','MANT','MANU','MAR','MARA','MARK','MAS','MASI','MAT','MATW','MATX','MAXR','MBB','MBI','MBIO','MBT','MBUU','MBWM','MC','MCBC','MCC','MCD','MCEP','MCF','MCFT','MCHI','MCHP','MCHX','MCK','MCO','MCRB','MCRI','MCRN','MCS','MCY','MD','MDB','MDC','MDCA','MDCO','MDGL','MDIV','MDLZ','MDP','MDR','MDRX','MDSO','MDT','MDU','MDY','MED','MEDP','MEET','MEI','MEIP','MELI','MEOH','MERC','MESA','MESO','MET','MEXX','MFA','MFC','MFG','MFGP','MFIN','MG','MGA','MGC','MGEE','MGI','MGIC','MGK','MGLN','MGM','MGNX','MGP','MGPI','MGRC','MGTA','MGTX','MGV','MGY','MHK','MHLD','MHO','MIC','MIDD','MIDU','MIDZ','MIK','MIME','MIND','MINI','MITK','MITT','MJ','MKC','MKL','MKSI','MKTX','MLCO','MLHR','MLI','MLM','MLND','MLNT','MLNX','MLPA','MLPI','MLPX','MLR','MMC','MMI','MMLP','MMM','MMP','MMS','MMSI','MMYT','MN','MNK','MNKD','MNOV','MNR','MNRO','MNST','MNTA','MNTX','MO','MOAT','MOBL','MOD','MODN','MOG_A','MOH','MOMO','MOO','MORN','MOS','MOV','MPAA','MPC','MPLX','MPW','MPWR','MPX','MR','MRC','MRCC','MRCY','MRK','MRKR','MRLN','MRNA','MRNS','MRO','MRTN','MRTX','MRVL','MS','MSA','MSB','MSCI','MSEX','MSFT','MSG','MSGN','MSI','MSM','MSON','MSTR','MT','MTB','MTCH','MTD','MTDR','MTG','MTH','MTL','MTN','MTOR','MTRN','MTRX','MTSC','MTSI','MTW','MTX','MTZ','MU','MUB','MUFG','MUNI','MUR','MUSA','MUX','MVC','MVIS','MVO','MWA','MX','MXI','MXIM','MXL','MYE','MYGN','MYL','MYOK','MYOV','MYRG','MYY','MZZ','NAK','NANO','NANR','NAT','NATI','NAV','NAVB','NAVI','NBEV','NBHC','NBIX','NBL','NBLX','NBR','NBRV','NBTB','NCLH','NCMI','NCR','NCTY','NDAQ','NDLS','NDSN','NE','NEE','NEM','NEO','NEOG','NEOS','NEP','NEPT','NERD','NERV','NET','NEU','NEW','NEWM','NEWR','NEWT','NFBK','NFG','NFLX','NG','NGD','NGG','NGHC','NGL','NGS','NGVC','NGVT','NH','NHC','NHI','NHTC','NI','NIB','NICE','NIHD','NINE','NIO','NJR','NK','NKE','NKTR','NL','NLNK','NLS','NLSN','NLTX','NLY','NM','NMFC','NMIH','NMM','NMR','NMRK','NNBR','NNI','NNN','NOA','NOAH','NOC','NOG','NOK','NOMD','NOV','NOVT','NOW','NP','NPO','NPTN','NR','NRG','NRP','NRT','NRZ','NS','NSA','NSC','NSIT','NSP','NSSC','NSTG','NTAP','NTCT','NTEC','NTES','NTGN','NTGR','NTLA','NTNX','NTP','NTR','NTRA','NTRP','NTRS','NTUS','NTWK','NUAN','NUE','NUGT','NUS','NUVA','NVAX','NVCR','NVDA','NVEE','NVGS','NVMI','NVO','NVRO','NVS','NVT','NVTA','NVTR','NWBI','NWE','NWL','NWN','NWPX','NWS','NWSA','NX','NXGN','NXPI','NXRT','NXST','NXTD','NYCB','NYMT','NYMX','NYT','O','OAS','OBE','OC','OCFC','OCN','OCSI','OCSL','OCUL','OCX','ODFL','ODP','ODT','OEC','OEF','OESX','OFC','OFG','OFIX','OGE','OGI','OGS','OHI','OI','OIH','OII','OIL','OILD','OILU','OIS','OKE','OKTA','OLED','OLLI','OLN','OLP','OMC','OMCL','OMER','OMEX','OMF','OMI','OMN','OMP','ONB','ONCE','ONDK','ONVO','OOMA','OPB','OPI','OPK','OPRX','OPY','OR','ORA','ORAN','ORBC','ORC','ORCL','ORI','ORIT','ORLY','ORMP','ORN','OSBC','OSG','OSIS','OSK','OSPN','OSTK','OSUR','OTEX','OTIC','OTTR','OUNZ','OUSA','OUT','OXFD','OXM','OXSQ','OXY','OZK','PAA','PAAS','PACB','PACW','PAG','PAGP','PAGS','PAHC','PAM','PANW','PAR','PARR','PATK','PAYC','PAYS','PAYX','PB','PBA','PBCT','PBF','PBFX','PBH','PBI','PBPB','PBR','PBR_A','PBT','PBW','PBYI','PCAR','PCEF','PCG','PCH','PCOM','PCRX','PCSB','PCTI','PCTY','PCY','PCYG','PCYO','PD','PDBC','PDCE','PDCO','PDD','PDFS','PDLI','PDM','PDP','PDS','PE','PEB','PEBO','PEG','PEGA','PEGI','PEI','PEIX','PEK','PEN','PENN','PEO','PEP','PER','PERI','PESI','PETQ','PETS','PEY','PEZ','PFBC','PFE','PFF','PFG','PFGC','PFLT','PFM','PFMT','PFNX','PFPT','PFS','PFSI','PFSW','PG','PGC','PGF','PGJ','PGNX','PGR','PGRE','PGTI','PGX','PH','PHB','PHDG','PHG','PHM','PHO','PHX','PI','PICO','PID','PIE','PII','PIN','PINC','PINS','PIRS','PIZ','PJC','PJP','PJT','PK','PKE','PKG','PKI','PKOH','PKW','PKX','PLAB','PLAN','PLAY','PLCE','PLD','PLNT','PLOW','PLSE','PLT','PLUG','PLUS','PLX','PLXS','PLYA','PM','PMT','PNC','PNFP','PNM','PNNT','PNQI','PNR','PNTG','PNW','PODD','POL','POOL','POR','POST','POTX','POWI','POWL','PPBI','PPC','PPDF','PPG','PPH','PPL','PQG','PRA','PRAA','PRAH','PRCP','PRF','PRFT','PRFZ','PRGO','PRGS','PRGX','PRI','PRIM','PRK','PRLB','PRMW','PRN','PRNB','PRO','PRQR','PRSC','PRSP','PRTA','PRTK','PRTY','PRU','PRVB','PS','PSA','PSB','PSCH','PSDO','PSEC','PSL','PSMT','PSN','PSNL','PSO','PSP','PSQ','PST','PSTG','PSTI','PSX','PSXP','PTC','PTCT','PTE','PTEN','PTF','PTH','PTI','PTLA','PTMN','PTON','PTR','PTVCB','PUK','PUMP','PVAC','PVG','PVH','PVL','PVTL','PWFL','PWR','PXD','PXH','PXI','PXJ','PXLW','PYPL','PYX','PZA','PZN','PZZA','QABA','QADA','QCOM','QCRH','QD','QDEL','QEP','QGEN','QHC','QID','QIWI','QLD','QLYS','QNST','QQEW','QQQ','QQQE','QRTEA','QRVO','QSR','QTEC','QTNT','QTS','QTT','QTWO','QUAD','QUIK','QUOT','QURE','R','RACE','RAD','RADA','RAIL','RAMP','RARE','RARX','RAVE','RAVN','RBA','RBBN','RBC','RBCAA','RBS','RCI','RCII','RCKT','RCL','RCM','RCMT','RCUS','RDFN','RDHL','RDI','RDN','RDNT','RDS_A','RDS_B','RDUS','RDWR','RDY','RE','REAL','RECN','REDU','REED','REFR','REG','REGI','REGN','REI','REK','RELL','REMX','RENN','REPH','RES','RESI','RESN','RETA','RETL','REV','REVG','REW','REXR','REZ','REZI','RF','RFIL','RFL','RFP','RGA','RGEN','RGLD','RGLS','RGNX','RGR','RGS','RH','RHI','RHP','RICK','RIG','RIGL','RILY','RING','RIO','RIOT','RJA','RJF','RJI','RJN','RL','RLGT','RLGY','RLH','RLI','RLJ','RM','RMAX','RMBS','RMD','RMTI','RNET','RNG','RNR','RNST','RNWK','ROBO','ROCK','ROG','ROIC','ROK','ROKU','ROL','ROLL','ROM','ROP','ROST','ROYT','RP','RPAI','RPD','RPG','RPM','RPT','RPV','RRC','RRD','RRGB','RRR','RS','RSG','RSP','RST','RSX','RTEC','RTH','RTIX','RTLR','RTN','RTRX','RTW','RUBI','RUBY','RUN','RUSHA','RUSL','RUSS','RUTH','RVLV','RVNC','RVSB','RWJ','RWK','RWL','RWM','RWO','RWR','RWT','RWX','RXL','RXN','RY','RYAAY','RYAM','RYB','RYH','RYI','RYN','RYTM','S','SA','SAA','SABR','SAFE','SAFM','SAFT','SAGE','SAH','SAIA','SAIC','SAIL','SALT','SAM','SAN','SAND','SANM','SANW','SAP','SASR','SATS','SAVE','SB','SBAC','SBBP','SBCF','SBGI','SBGL','SBH','SBIO','SBLK','SBNY','SBRA','SBS','SBSI','SBUX','SC','SCCO','SCHA','SCHB','SCHC','SCHD','SCHE','SCHF','SCHG','SCHH','SCHL','SCHM','SCHN','SCHP','SCHV','SCHW','SCHX','SCI','SCIF','SCJ','SCL','SCM','SCO','SCOM','SCOR','SCPL','SCS','SCSC','SCU','SCVL','SCWX','SCYX','SCZ','SD','SDC','SDIV','SDOW','SDR','SDRL','SDS','SDT','SDY','SE','SEA','SEAC','SEAS','SECO','SEDG','SEE','SEF','SEIC','SELB','SEM','SEMG','SENS','SERV','SESN','SF','SFBS','SFE','SFIX','SFL','SFM','SFNC','SFUN','SGC','SGEN','SGG','SGH','SGMO','SGMS','SGOL','SGRY','SGU','SH','SHAK','SHEN','SHLO','SHLX','SHO','SHOO','SHOP','SHW','SHY','SHYG','SIBN','SID','SIEB','SIEN','SIFY','SIG','SIGA','SIGI','SIL','SILJ','SILK','SILV','SIMO','SINA','SIRI','SITC','SITE','SIVB','SIVR','SIX','SIZE','SJB','SJI','SJM','SJNK','SJR','SJT','SJW','SKF','SKM','SKT','SKX','SKY','SKYW','SKYY','SLAB','SLB','SLCA','SLDB','SLF','SLG','SLGN','SLM','SLP','SLRC','SLV','SLX','SM','SMAR','SMED','SMFG','SMG','SMH','SMLP','SMMT','SMN','SMOG','SMP','SMPL','SMRT','SMSI','SMTC','SMTX','SNA','SNAP','SNBR','SNCR','SND','SNDL','SNDR','SNDX','SNE','SNH','SNLN','SNN','SNP','SNPS','SNR','SNSS','SNV','SNX','SNY','SO','SOCL','SOGO','SOHU','SOI','SOL','SOLO','SON','SONO','SORL','SOXL','SOXS','SOXX','SOYB','SP','SPAR','SPB','SPDN','SPDW','SPEM','SPG','SPGI','SPH','SPHB','SPHD','SPHQ','SPHS','SPKE','SPLG','SPLK','SPLV','SPNE','SPNS','SPOK','SPOT','SPPI','SPR','SPRO','SPRT','SPSC','SPSM','SPTM','SPTN','SPWH','SPWR','SPXC','SPXL','SPXS','SPXU','SPY','SPYG','SPYV','SQ','SQBG','SQM','SQQQ','SR','SRAX','SRC','SRCE','SRCI','SRCL','SRDX','SRE','SREV','SRG','SRI','SRL','SRLP','SRNE','SRPT','SRRA','SRS','SRT','SRTY','SSB','SSD','SSI','SSL','SSNC','SSO','SSP','SSRM','SSSS','SSTK','SSW','SSYS','ST','STAA','STAG','STAR','STAY','STBA','STC','STCN','STE','STFC','STI','STKL','STL','STLD','STM','STML','STMP','STNE','STNG','STON','STOR','STRA','STRL','STT','STWD','STX','STZ','SU','SUI','SUM','SUN','SUNS','SUP','SUPN','SUPV','SUSL','SVC','SVMK','SVRA','SVVC','SVXY','SWAV','SWCH','SWI','SWIR','SWK','SWKS','SWM','SWN','SWX','SXC','SXI','SXT','SY','SYBX','SYF','SYK','SYKE','SYMC','SYNA','SYNC','SYNH','SYNL','SYRS','SYX','SYY','T','TA','TACO','TACT','TAK','TAL','TALO','TAN','TAO','TAOP','TAP','TARO','TAST','TBBK','TBF','TBI','TBK','TBNK','TBPH','TBT','TCBI','TCBK','TCDA','TCF','TCMD','TCO','TCP','TCPC','TCRD','TCRR','TCS','TCX','TD','TDC','TDG','TDIV','TDOC','TDS','TDW','TDY','TEAM','TECD','TECH','TECK','TECL','TECS','TEF','TEL','TELL','TEN','TENB','TEO','TER','TERP','TEUM','TEVA','TEX','TFI','TFSL','TFX','TG','TGB','TGE','TGH','TGI','TGNA','TGP','TGS','TGT','TGTX','THC','THCX','THD','THFF','THG','THO','THOR','THR','THRM','THS','TIF','TILE','TIP','TISI','TITN','TIVO','TJX','TK','TKC','TKR','TLGT','TLH','TLND','TLRA','TLRD','TLRY','TLT','TLYS','TM','TME','TMF','TMHC','TMO','TMP','TMQ','TMST','TMUS','TMV','TNA','TNAV','TNC','TNDM','TNET','TNK','TNP','TOCA','TOL','TOO','TORC','TOT','TOUR','TOWN','TPB','TPC','TPCO','TPH','TPIC','TPR','TPRE','TPTX','TPVG','TPX','TQQQ','TR','TRC','TREC','TREE','TREX','TRGP','TRHC','TRI','TRIB','TRIL','TRIP','TRMB','TRMK','TRN','TRNO','TROW','TROX','TRP','TRQ','TRS','TRST','TRTN','TRTX','TRU','TRUE','TRUP','TRV','TRVG','TRVN','TRWH','TRX','TRXC','TS','TSCO','TSE','TSEM','TSG','TSLA','TSLX','TSM','TSN','TSQ','TSU','TTC','TTD','TTEC','TTEK','TTGT','TTI','TTM','TTMI','TTNP','TTOO','TTS','TTT','TTWO','TU','TUFN','TUP','TUR','TURN','TUSK','TV','TVTY','TW','TWI','TWIN','TWLO','TWM','TWNK','TWO','TWOU','TWST','TWTR','TX','TXMD','TXN','TXRH','TXT','TYD','TYL','TYME','TYO','TZA','TZOO','UA','UAA','UAL','UAMY','UAN','UBA','UBER','UBIO','UBNK','UBS','UBSI','UBT','UBX','UCBI','UCFC','UCO','UCOM','UCTT','UDN','UDOW','UDR','UE','UEC','UEIC','UEPS','UFCS','UFI','UFPI','UFS','UGA','UGI','UGL','UGP','UHS','UHT','UI','UIHC','UIS','UL','ULBI','ULE','ULTA','UMBF','UMC','UMDD','UMH','UMPQ','UN','UNF','UNFI','UNG','UNH','UNIT','UNL','UNM','UNP','UNT','UNVR','UPLD','UPRO','UPS','UPWK','URA','URBN','URE','URGN','URI','URTH','URTY','USAC','USAK','USB','USCR','USD','USDU','USFD','USIG','USL','USM','USMC','USNA','USO','USOD','USOU','USPH','UST','USX','UTHR','UTI','UTL','UTSI','UTX','UUP','UUUU','UVE','UVSP','UVV','UVXY','UWM','UXIN','UYG','UYM','V','VAC','VAL','VALE','VAR','VAW','VB','VBIV','VBK','VBLT','VBR','VBTX','VC','VCEL','VCIT','VCLT','VCR','VCRA','VCYT','VDC','VDE','VEA','VEC','VECO','VEDL','VEEV','VEON','VER','VERI','VERU','VET','VEU','VFC','VFF','VFH','VG','VGK','VGR','VGT','VGZ','VHC','VHT','VIA','VIAB','VIAV','VICI','VICR','VIG','VIIX','VIPS','VIRT','VIS','VIV','VIVO','VIXM','VIXY','VJET','VKTX','VLO','VLRS','VLY','VMC','VMI','VMW','VNDA','VNE','VNET','VNO','VNOM','VNQ','VNQI','VNTR','VO','VOC','VOD','VOE','VOLT','VONV','VOO','VOT','VOX','VOXX','VOYA','VPG','VPL','VPU','VRA','VRAY','VREX','VRML','VRNS','VRNT','VRP','VRRM','VRS','VRSK','VRSN','VRTU','VRTV','VRTX','VSAT','VSH','VSI','VSLR','VSS','VST','VSTM','VSTO','VT','VTI','VTNR','VTR','VTV','VTWO','VUG','VUZI','VV','VVI','VVUS','VVV','VWO','VXF','VXUS','VYGR','VYM','VZ','W','WAB','WABC','WAFD','WAIR','WAL','WASH','WAT','WATT','WB','WBA','WBAI','WBC','WBS','WBT','WCC','WCG','WCN','WD','WDAY','WDC','WDFC','WDR','WEAT','WEC','WELL','WEN','WERN','WES','WETF','WEX','WFC','WGO','WH','WHD','WHG','WHR','WIFI','WING','WIRE','WIT','WIX','WK','WLDN','WLH','WLK','WLKP','WLL','WLTW','WM','WMB','WMC','WMGI','WMK','WMS','WMT','WNC','WNEB','WNS','WOOD','WOR','WORK','WOW','WPC','WPG','WPM','WPP','WPRT','WPS','WPX','WRB','WRE','WRI','WRK','WRLD','WRTC','WSBC','WSBF','WSC','WSFS','WSM','WSO','WSR','WST','WTBA','WTFC','WTI','WTR','WTRH','WTS','WTTR','WU','WUBA','WVE','WW','WWD','WWE','WWW','WY','WYND','WYNN','X','XAN','XAR','XBI','XBIT','XEC','XEL','XENE','XENT','XERS','XES','XHB','XHE','XHR','XIN','XLB','XLC','XLE','XLF','XLI','XLK','XLNX','XLP','XLRE','XLRN','XLU','XLV','XLY','XME','XMLV','XNCR','XNET','XOG','XOM','XON','XONE','XOP','XPEL','XPER','XPH','XPO','XPP','XRAY','XRF','XRT','XRX','XSD','XT','XXII','XYL','Y','YANG','YCBD','YCL','YCS','YELP','YETI','YEXT','YGYI','YINN','YMLP','YNDX','YOLO','YORW','YPF','YRCW','YRD','YUM','YUMC','YXI','YY','Z','ZAGG','ZAYO','ZBH','ZBIO','ZBRA','ZEN','ZEUS','ZFGN','ZG','ZGNX','ZION','ZIOP','ZIXI','ZLAB','ZM','ZN','ZNGA','ZNH','ZROZ','ZS','ZSL','ZTO','ZTS','ZUMZ','ZUO','ZVO','ZYME','ZYNE']

for smbl in codelist:
	try:
		stock = str("VOL/") + smbl
		stock_iv60 = quandl.get(stock.upper(), column_index='31')
		stock_hv60 = quandl.get(stock.upper(), column_index='4')
		hv60 = stock_hv60[['Hv60']].to_numpy()
		iv60 = stock_iv60[['IvMean60']].to_numpy()
		avgiv = np.average(iv60)
		avghv = np.average(hv60)
		medianiv = np.median(iv60)
		medianhv = np.median(hv60)
		medians.append((medianiv-medianhv)/medianhv)
		averages.append((avgiv - avghv)/avghv)
		print(stock + ' good')
	except:
		print(stock + ' bad')
		pass

for smbl in codelist2:
	try:
		stock = str("VOL/") + smbl
		stock_iv60 = quandl.get(stock.upper(), column_index='31')
		stock_hv60 = quandl.get(stock.upper(), column_index='4')
		hv60 = stock_hv60[['Hv60']].to_numpy()
		iv60 = stock_iv60[['IvMean60']].to_numpy()
		avgiv = np.average(iv60)
		avghv = np.average(hv60)
		medianiv = np.median(iv60)
		medianhv = np.median(hv60)
		medians.append((medianiv-medianhv)/medianhv)
		averages.append((avgiv - avghv)/avghv)
		print(stock + ' good')
	except:
		print(stock + ' bad')
		pass

print("Average Medians Difference")
print(format(mean(medians)*100,'.2f'))
print("Average Mean Difference")
print(format(mean(averages)*100,'.2f'))
print("Median Medians Difference")
print(format(median(medians)*100,'.2f'))
print("Median Mean Difference")
print(format(median(averages)*100,'.2f'))