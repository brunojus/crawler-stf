CREATE DATABASE  IF NOT EXISTS `stf` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `stf`;
-- MySQL dump 10.16  Distrib 10.1.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: stf
-- ------------------------------------------------------
-- Server version	10.1.34-MariaDB-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `processos`
--

LOCK TABLES `processos` WRITE;
/*!40000 ALTER TABLE `processos` DISABLE KEYS */;
INSERT INTO `processos` VALUES (146,'08/06/2009','Baixa ao arquivo do STF, Guia nº',' ','Guia 8945 - SEÇÃO DE ARQUIVO','\n                                             '),(147,'05/06/2009','Transitado(a) em julgado',' ','em 04 de junho de 2009. Acórdão/decisão de 18/05/2009.','\n                                             '),(148,'25/05/2009','Publicação, DJE',' ','Decisão de 18/05/2009 - DJE nº 95, divulgado em 22/05/2009','\n                                             '),(149,'18/05/2009','Prejudicado','MIN. JOAQUIM BARBOSA','\"[...] Publique-se. Arquive-se.\"','\n                                             '),(150,'24/01/2005','CONCLUSOS AO RELATOR',' ',' \n                                        ','\n                                             '),(151,'11/01/2005','JUNTADA',' ','INTIMAÇÃO VIA POSTAL DEVOLVIDA PELA ECT POR SER DESCONHECIDO NO ENDEREÇO O SR. EDUARDO ALVES FERREIRA','\n                                             '),(152,'11/01/2005','JUNTADA',' ','INTIMAÇÃO VIA POSTAL DEVOLVIDA PELA ECT POR TER FALECIDO O SR. MARCOS DAMASCENO CRONENBERGER','\n                                             '),(153,'11/01/2005','JUNTADA',' ','INTIMAÇÃO VIA POSTAL DEVOLVIDA PELA ECT POR TER-SE MUDADO O SR. DARVIN PESTANA FILHO','\n                                             '),(154,'11/01/2005','JUNTADA',' ','INTIMAÇÃO VIA POSTAL DEVOLVIDA PELA ECT POR ENCONTRAR-SE AUSENTE (3X) 0 SR. LAURO HEBERT DE ARAÚJO SILVA','\n                                             '),(155,'11/01/2005','JUNTADA DE AVISO DE RECEBIMENTO',' ','REF. CITAÇÃO DE LAÉRCIO EULÁLIO DE ARAÚJO LIMA, EM TERESINA/PI','\n                                             '),(156,'11/01/2005','JUNTADA DE AVISO DE RECEBIMENTO',' ','REF. CITAÇÃO DE MARCELO RODRIGUES PORTELA NUNES, EM TERESINA/PI','\n                                             '),(157,'11/01/2005','JUNTADA DE AVISO DE RECEBIMENTO',' ','REF. CITAÇÃO DE JUIZ TIBÉRIO FREIRE VILLAR DA SILVA, EM TERESINA/PI','\n                                             '),(158,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','A EDUARDO ALVES FERREIRA, EM TERESINA/PI','\n                                             '),(159,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','A LAURO HEBERT DE ARAÚJO SILVA, EM TERESINA/PI','\n                                             '),(160,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','A LAÉRCIO EULÁLIO DE ARAÚJO LIMA, EM TERESINA/PI','\n                                             '),(161,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','AO JUIZ TIBÉRIO FREIRE VILLAR DA SILVA, EM TERESINA/PI','\n                                             '),(162,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','A MARCOS DAMASCENO CRONENBERGER OU MARCUS DAMASCENO CRONENBERGER OU MARCUS DAMASCENO CRONENBERGER, EM TERESINA/PI','\n                                             '),(163,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','A DARVIN PESTANA FILHO, EM TERESINA/PI','\n                                             '),(164,'03/12/2004','EXPEDIDA INTIMACAO VIA POSTAL',' ','A MARCELO RODRIGUES PORTELA NUNES, EM TERESINA/PI','\n                                             '),(165,'29/11/2004','PUBLICACAO, DJ:',' ','DECISÃO DE 19.11.2004. ','\n                                             '),(166,'23/11/2004','DECISÃO LIMINAR - INDEFERIDA',' ','EM 19.11.2004: CITEM-SE. PUBLIQUE-SE.','\n                                             '),(167,'17/11/2004','CONCLUSOS AO RELATOR',' ',' \n                                        ','\n                                             '),(168,'17/11/2004','JUNTADA',' ','PG/STF Nº 121044/2004. COM DESPACHO DE 17/11/04: JUNTE-SE.','\n                                             '),(169,'16/11/2004','PETIÇÃO',' ','AVULSA Nº 121044/2004 DO ESTADO DO PIAUÍ PRESTANDO ESCLARECIMENTOS E REITERANDO O PEDIDO DE LIMINAR. AO MINISTRO RELATOR.','\n                                             '),(170,'12/11/2004','CONCLUSOS AO RELATOR',' ',' \n                                        ','\n                                             '),(171,'12/11/2004','JUNTADA',' ','PG/STF Nº 119810/2004, COM DESPACHO: JUNTE-SE.','\n                                             '),(172,'11/11/2004','PETIÇÃO',' ','AVULSA Nº 119810/2004 DE DARVIN PESTANA FILHO E OUTROS REQUERENDO A IMPROCEDÊNCIA DO PEDIDO LIMINAR E DA AÇÃO CAUTELAR. AO MINISTRO RELATOR.','\n                                             '),(173,'08/11/2004','CONCLUSOS AO RELATOR',' ',' \n                                        ','\n                                             '),(174,'08/11/2004','DISTRIBUIDO POR PREVENCAO',' ','MIN. JOAQUIM BARBOSA','\n                                             ');
/*!40000 ALTER TABLE `processos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-12  0:24:08
