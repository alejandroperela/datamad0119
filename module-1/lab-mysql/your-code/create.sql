-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customers` (
  `idCustomers` INT NOT NULL AUTO_INCREMENT,
  `CustomerID` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Phone` INT NULL,
  `Email` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State/province` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `Zip` INT NULL,
  PRIMARY KEY (`idCustomers`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Salesperson` (
  `StaffID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`StaffID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoices` (
  `idInvoices` INT NOT NULL AUTO_INCREMENT,
  `Number` INT NOT NULL,
  `Date` DATETIME NULL,
  `Car` VARCHAR(45) NULL,
  `Customer` VARCHAR(45) NULL,
  `Salesperson_idSalesperson` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  `Salesperson_StaffID` INT NOT NULL,
  PRIMARY KEY (`idInvoices`),
  INDEX `fk_Invoices_Customers1_idx` (`Customers_idCustomers` ASC),
  INDEX `fk_Invoices_Salesperson1_idx` (`Salesperson_StaffID` ASC),
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `mydb`.`customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salesperson1`
    FOREIGN KEY (`Salesperson_StaffID`)
    REFERENCES `mydb`.`Salesperson` (`StaffID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cars` (
  `idCars` INT NOT NULL AUTO_INCREMENT,
  `VIN` VARCHAR(100) NOT NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` INT NULL,
  `Color` VARCHAR(45) NULL,
  `Invoices_idInvoices` INT NOT NULL,
  `customers_idCustomers` INT NOT NULL,
  `Salesperson_idSalesperson` INT NOT NULL,
  `Salesperson_StaffID` INT NOT NULL,
  INDEX `fk_Cars_Invoices1_idx` (`Invoices_idInvoices` ASC),
  INDEX `fk_Cars_customers1_idx` (`customers_idCustomers` ASC),
  PRIMARY KEY (`idCars`),
  INDEX `fk_Cars_Salesperson1_idx` (`Salesperson_StaffID` ASC),
  CONSTRAINT `fk_Cars_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `mydb`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Cars_customers1`
    FOREIGN KEY (`customers_idCustomers`)
    REFERENCES `mydb`.`customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Cars_Salesperson1`
    FOREIGN KEY (`Salesperson_StaffID`)
    REFERENCES `mydb`.`Salesperson` (`StaffID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customers_has_Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customers_has_Salesperson` (
  `customers_idCustomers` INT NOT NULL,
  `Salesperson_idSalesperson` INT NOT NULL,
  `Salesperson_StaffID` INT NOT NULL,
  PRIMARY KEY (`customers_idCustomers`, `Salesperson_idSalesperson`),
  INDEX `fk_customers_has_Salesperson_customers1_idx` (`customers_idCustomers` ASC),
  INDEX `fk_customers_has_Salesperson_Salesperson1_idx` (`Salesperson_StaffID` ASC),
  CONSTRAINT `fk_customers_has_Salesperson_customers1`
    FOREIGN KEY (`customers_idCustomers`)
    REFERENCES `mydb`.`customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_customers_has_Salesperson_Salesperson1`
    FOREIGN KEY (`Salesperson_StaffID`)
    REFERENCES `mydb`.`Salesperson` (`StaffID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

