USE DemoDB;

CREATE TABLE `DemoDB`.`Demo_property` (
  `parcelid` INT NOT NULL,
  `actype` INT NULL,
  `archstyle` INT NULL,
  `basementsqft` DECIMAL(10,2) NULL,
  `bathroomcnt` DECIMAL(5,2) NULL,
  `bedroomcnt` INT NULL,
  `buildingclasstype` INT NULL,
  `buildingqualitytype` INT NULL,
  `calculatedbathnbr` DECIMAL(5,2) NULL,
  `decktype` INT NULL,
  `finishedfloor1sqft` INT NULL,
  `totalfinishedsqft` INT NULL,
  `finishedsqft12` INT NULL,
  `finishedsqft13` INT NULL,
  `finishedsqft15` INT NULL,
  `finishedsqft50` INT NULL,
  `finishedsqft6` INT NULL,
  `fips` INT NULL,
  `fireplacecnt` INT NULL,
  `fullbathcnt` INT NULL,
  `garagecarcnt` INT NULL,
  `garagetotalsqft` INT NULL,
  `hottuborspa` TINYINT NULL,
  `heatingsystemtype` INT NULL,
  `lotsizesqft` INT NULL,
  `poolcnt` INT NULL,
  `poolsizesum` INT NULL,
  `pooltype10` INT NULL,
  `pooltype2` INT NULL,
  `pooltype7` INT NULL,
  `countylandusecode` VARCHAR(10) NULL,
  `landusetype` INT NULL,
  `zoningdesc` VARCHAR(10) NULL,
  `rawcensustractandblock` VARCHAR(21) NULL,
  `regionidcity` INT NULL,
  `regionidcounty` INT NULL,
  `regionidneighborhood` INT NULL,
  `regionidzip` VARCHAR(6) NULL,
  `roomcnt` INT NULL,
  `storytypeid` INT NULL,
  `threequarterbathnbr` INT NULL,
  `constructiontype` INT NULL,
  `unitcnt` INT NULL,
  `yardbuildingsqft17` INT NULL,
  `yardbuildingsqft26` INT NULL,
  `yearbuilt` INT NULL,
  `noofstories` INT NULL,
  `fireplaceflag` TINYINT NULL,
  `structuretaxvalue` INT NULL,
  `taxvalue` INT NULL,
  `assessmentyear` INT NULL,
  `landtaxvalue` INT NULL,
  `taxamount` DECIMAL(10,2) NULL,
  `taxdelinquencyflag` TINYINT NULL,
  `taxdelinquencyyear` INT NULL,
  `censustractandblock` VARCHAR(14) NULL,
  PRIMARY KEY (`parcelid`),
  UNIQUE INDEX `idproperty_UNIQUE` (`parcelid` ASC) VISIBLE);

CREATE TABLE `DemoDB`.`Demo_label` (
  `parcelid` INT(11) NOT NULL,
  `logerror` DECIMAL(10,9) NULL,
  `transactiondate` DATE NULL,
  PRIMARY KEY (`parcelid`),
  UNIQUE INDEX `parcelid_UNIQUE` (`parcelid` ASC) VISIBLE);