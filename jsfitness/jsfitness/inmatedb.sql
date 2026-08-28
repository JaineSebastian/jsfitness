/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - jfitness
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE `jfitness`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `time_slot_id` int(11) DEFAULT NULL,
  `trainer_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `eqmt_id` int(11) DEFAULT NULL,
  `catgory_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`time_slot_id`,`trainer_id`,`user_id`,`eqmt_id`,`catgory_id`,`amount`) values 
(1,1,8,6,7,7,'500'),
(2,1,8,8,7,8,'500');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `catgory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`catgory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`catgory_id`,`category_name`) values 
(8,'strength training'),
(7,'cardiac vascular');

/*Table structure for table `circuit_sub` */

DROP TABLE IF EXISTS `circuit_sub`;

CREATE TABLE `circuit_sub` (
  `c_sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `workout_id` int(11) DEFAULT NULL,
  `times` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`c_sub_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `circuit_sub` */

insert  into `circuit_sub`(`c_sub_id`,`c_id`,`workout_id`,`times`) values 
(2,1,1,'12');

/*Table structure for table `circuits` */

DROP TABLE IF EXISTS `circuits`;

CREATE TABLE `circuits` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(100) DEFAULT NULL,
  `purpose` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `circuits` */

insert  into `circuits`(`c_id`,`c_name`,`purpose`) values 
(1,'jumping','burn calories');

/*Table structure for table `equipments` */

DROP TABLE IF EXISTS `equipments`;

CREATE TABLE `equipments` (
  `eqmt_id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `equp_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`eqmt_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `equipments` */

insert  into `equipments`(`eqmt_id`,`image`,`equp_name`) values 
(7,'static/983b1d56-75b0-488b-b613-1d151422372eimages.jpg','Ade Machine'),
(8,'static/af49d607-d436-4895-8310-ff67d204f8dbimages.jpg','Bench');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`) values 
(1,1,'rtr'),
(2,1,'hi'),
(3,1,'hello'),
(4,1,'dsds'),
(5,1,'sadsadasd'),
(6,1,'dfgth');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','123','admin'),
(2,'triner1','triner1','trainer'),
(18,'trainer4','trainer4','trainer'),
(17,'trainer3','trainer3','trainer'),
(16,'trainer2','trainer2','trainer'),
(15,'user','123','user');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `timeslots` */

DROP TABLE IF EXISTS `timeslots`;

CREATE TABLE `timeslots` (
  `time_slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) DEFAULT NULL,
  `from_time` varchar(100) DEFAULT NULL,
  `to_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`time_slot_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `timeslots` */

insert  into `timeslots`(`time_slot_id`,`date`,`from_time`,`to_time`) values 
(2,'2024-02-10','12.30 pm','4:00 pm'),
(8,'2024-02-12','12.30 pm','4:07 pm'),
(9,'2024-02-12','12.30 pm','4:07 pm');

/*Table structure for table `trainer` */

DROP TABLE IF EXISTS `trainer`;

CREATE TABLE `trainer` (
  `trainer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `register_number` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`trainer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `trainer` */

insert  into `trainer`(`trainer_id`,`login_id`,`name`,`email`,`phone`,`register_number`,`district`,`image`,`status`) values 
(6,17,'james rodirigus','jmerodi@gmail.com','3432434','1238','KANNUR','static/images/c8631da6-7508-49cc-88a1-cf1748a07342software-engineer.png','pending'),
(8,18,'Edwin','in@gmial.com','7306033950','1238','ernklm','static/images/30f7c27a-9b45-4da1-9671-872785461f8ddriver1.jpeg','pending');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `weight` varchar(100) DEFAULT NULL,
  `height` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`name`,`email`,`phone`,`weight`,`height`) values 
(1,15,'ASHIQ C','+916235707708','ashiquaq1212@gmail.com','55','56');

/*Table structure for table `workouts` */

DROP TABLE IF EXISTS `workouts`;

CREATE TABLE `workouts` (
  `workout_id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`workout_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `workouts` */

insert  into `workouts`(`workout_id`,`image`,`name`,`description`) values 
(1,'static/images/jumping-jack.gif','cardiac','for chest'),
(2,'static/images/high knee.gif','Flick','High Knee'),
(3,'static/images/pumbing.gif','Flick','Pumbing');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
