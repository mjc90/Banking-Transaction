-- -----------------------------------------------------
-- Schema banking_system
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `banking_system` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `banking_system` ;

-- -----------------------------------------------------
-- Table `banking_system`.`accounts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banking_system`.`accounts` (
  `account_number` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `dob` DATE NOT NULL,
  `balance` FLOAT NOT NULL DEFAULT '0',
  PRIMARY KEY (`account_number`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;