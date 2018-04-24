--
-- Database: `urenloop`
--

DROP TABLE IF EXISTS `teams`;
DROP TABLE IF EXISTS `laps`;

CREATE TABLE  `teams` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR( 255 ) NOT NULL,
    `laps` INTEGER NOT NULL
);

CREATE TABLE `laps` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `team_id` INTEGER NOT NULL,
    `value` INTEGER NOT NULL,
    `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Sample teams

INSERT INTO `teams` (`id`, `name`, `laps`) VALUES
(1, 'HILOK', 0),
(2, 'VTK', 0),
(3, 'VEK', 0),
(4, 'VGK', 0),
(5, 'Hermes, Veto & Lila', 0),
(6, 'SK', 0),
(7, 'WVK', 0),
(8, 'HK', 0),
(9, 'Politea', 0),
(10, 'VPPK & Moeder Lies', 0),
(11, 'Wetenschappen & VLAK', 0),
(12, 'VRG', 0),
(13, 'Charpa', 0),
(14, 'VLK', 0),
(15, 'VDK & Pharma', 0),
(16, 'VBK', 0),
(17, 'Blandinia', 0)

-- (1, 'HILOK', 0),
-- (2, 'VGK', 0),
-- (3, 'VTK', 0),
-- (4, 'VLK', 0),
-- (5, 'VRG', 0),
-- (6, 'VEK & Moeder Lies', 0),
-- (7, 'VPPK', 0),
-- (8, 'Hermes & LILA', 0),
-- (9, 'Wetenschappen & VLAK', 0),
-- (10, 'VBK', 0),
-- (11, 'HK', 0),
-- (12, 'SK', 0),
-- (13, 'Zeus WPI', 0);
