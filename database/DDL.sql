-- MySQL Script generated by MySQL Workbench
-- Wed Apr 27 11:09:16 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

-- CS 340 Project Step 2 Draft: Normalized Schema + DDL with Sample Data
-- Aaron Trinh and Eric Tolson

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Table `Customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Customers` ;

CREATE TABLE IF NOT EXISTS `Customers` (
  `customerID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(145) NOT NULL,
  `email` VARCHAR(145) NOT NULL,
  `phone_num` BIGINT(10) NOT NULL,
  `address` VARCHAR(145) NOT NULL,
  PRIMARY KEY (`customerID`),
  UNIQUE INDEX `customerID_UNIQUE` (`customerID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Discounts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Discounts` ;

CREATE TABLE IF NOT EXISTS `Discounts` (
  `discountID` INT NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(145) NOT NULL,
  `percent_off` INT NOT NULL,
  PRIMARY KEY (`discountID`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Drivers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Drivers` ;

CREATE TABLE IF NOT EXISTS `Drivers` (
  `driverID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`driverID`),
  UNIQUE INDEX `driverID_UNIQUE` (`driverID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Items` ;

CREATE TABLE IF NOT EXISTS `Items` (
  `itemID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(145) NOT NULL,
  `price` DECIMAL(19,2) NOT NULL,
  PRIMARY KEY (`itemID`),
  UNIQUE INDEX `itemID_UNIQUE` (`itemID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Order_Items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Order_Items` ;

CREATE TABLE IF NOT EXISTS `Order_Items` (
  `quantity` INT NOT NULL,
  `orderID` INT NOT NULL,
  `itemID` INT NOT NULL,
  `unit_price` DECIMAL(19,2) NOT NULL,
  `line_price` DECIMAL(19,2) NOT NULL,
  INDEX `fk_Order_Items_Orders1_idx` (`orderID` ASC) VISIBLE,
  INDEX `fk_Order_Items_Items1_idx` (`itemID` ASC) VISIBLE,
  CONSTRAINT `fk_Order_Items_Orders1`
    FOREIGN KEY (`orderID`)
    REFERENCES `Orders` (`orderID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Order_Items_Items1`
    FOREIGN KEY (`itemID`)
    REFERENCES `Items` (`itemID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Orders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Orders` ;

CREATE TABLE IF NOT EXISTS `Orders` (
  `orderID` INT NOT NULL AUTO_INCREMENT,
  `order_total` DECIMAL(19,2) NOT NULL,
  `is_delivery` TINYINT NOT NULL,
  `customerID` INT NOT NULL,
  `driverID` INT NULL,
  `discountID` INT NULL,
  `credit_card` BIGINT(16) NOT NULL,
  PRIMARY KEY (`orderID`),
  UNIQUE INDEX `orderID_UNIQUE` (`orderID` ASC) VISIBLE,
  INDEX `fk_Orders_Customers_idx` (`customerID` ASC) VISIBLE,
  INDEX `fk_Orders_Drivers1_idx` (`driverID` ASC) VISIBLE,
  INDEX `fk_Orders_Discounts1_idx` (`discountID` ASC) VISIBLE,
  CONSTRAINT `fk_Orders_Customers`
    FOREIGN KEY (`customerID`)
    REFERENCES `Customers` (`customerID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Orders_Drivers1`
    FOREIGN KEY (`driverID`)
    REFERENCES `Drivers` (`driverID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
    FOREIGN KEY (`discountID`)
    REFERENCES `Discounts` (`discountID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Data for table `Customers`
-- -----------------------------------------------------
START TRANSACTION;
INSERT INTO `Customers` (`customerID`, `name`, `email`, `phone_num`, `address`) VALUES (DEFAULT, 'Eric', 'eric@gmail.com', 1111111111, '123 Eric St ');
INSERT INTO `Customers` (`customerID`, `name`, `email`, `phone_num`, `address`) VALUES (DEFAULT, 'Aaron', 'aaron@gmail.com', 222222222, '123 Aaron St');
INSERT INTO `Customers` (`customerID`, `name`, `email`, `phone_num`, `address`) VALUES (DEFAULT, 'Jessica', 'Jessica@gmail.com', 333333333, '123 Jessica St');

COMMIT;


-- -----------------------------------------------------
-- Data for table `Discounts`
-- -----------------------------------------------------
START TRANSACTION;
INSERT INTO `Discounts` (`discountID`, `code`, `percent_off`) VALUES (DEFAULT, '15off', 15);
INSERT INTO `Discounts` (`discountID`, `code`, `percent_off`) VALUES (DEFAULT, 'spring', 5);
INSERT INTO `Discounts` (`discountID`, `code`, `percent_off`) VALUES (DEFAULT, 'buy2', 50);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Drivers`
-- -----------------------------------------------------
START TRANSACTION;
INSERT INTO `Drivers` (`driverID`, `name`) VALUES (DEFAULT, 'Charlie');
INSERT INTO `Drivers` (`driverID`, `name`) VALUES (DEFAULT, 'Mike');
INSERT INTO `Drivers` (`driverID`, `name`) VALUES (DEFAULT, 'Oscar');

COMMIT;


-- -----------------------------------------------------
-- Data for table `Items`
-- -----------------------------------------------------
START TRANSACTION;
INSERT INTO `Items` (`itemID`, `name`, `price`) VALUES (DEFAULT, 'Crispy Chicken', 18);
INSERT INTO `Items` (`itemID`, `name`, `price`) VALUES (DEFAULT, 'Yangnyeom Chicken', 20);
INSERT INTO `Items` (`itemID`, `name`, `price`) VALUES (DEFAULT, 'Soy Garlic Chicken', 20);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Order_Items`
-- -----------------------------------------------------
START TRANSACTION;
INSERT INTO `Order_Items` (`quantity`, `orderID`, `itemID`, `unit_price`, `line_price`) VALUES (2, 1, 1, 18, 36);
INSERT INTO `Order_Items` (`quantity`, `orderID`, `itemID`, `unit_price`, `line_price`) VALUES (2, 1, 2, 20, 40);
INSERT INTO `Order_Items` (`quantity`, `orderID`, `itemID`, `unit_price`, `line_price`) VALUES (2, 2, 1, 18, 36);
INSERT INTO `Order_Items` (`quantity`, `orderID`, `itemID`, `unit_price`, `line_price`) VALUES (2, 2, 2, 20, 40);
INSERT INTO `Order_Items` (`quantity`, `orderID`, `itemID`, `unit_price`, `line_price`) VALUES (2, 3, 2, 20, 40);
INSERT INTO `Order_Items` (`quantity`, `orderID`, `itemID`, `unit_price`, `line_price`) VALUES (2, 3, 3, 20, 40);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Orders`
-- -----------------------------------------------------
START TRANSACTION;
INSERT INTO `Orders` (`orderID`, `order_total`, `is_delivery`, `customerID`, `driverID`, `discountID`, `credit_card`) VALUES (DEFAULT, 64.6, 1, 1, 1, 1, 1111111111111111);
INSERT INTO `Orders` (`orderID`, `order_total`, `is_delivery`, `customerID`, `driverID`, `discountID`, `credit_card`) VALUES (DEFAULT, 72.2, 0, 2, NULL, 2, 2222222222222222);
INSERT INTO `Orders` (`orderID`, `order_total`, `is_delivery`, `customerID`, `driverID`, `discountID`, `credit_card`) VALUES (DEFAULT, 40, 1, 3, 3, 3, 3333333333333333);

COMMIT;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
