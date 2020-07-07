CREATE TABLE alembic_data_version
(
    version VARCHAR(40) PRIMARY KEY
);
CREATE UNIQUE INDEX alembic_data_version_version_uindex ON alembic_data_version (version);

INSERT INTO alembic_data_version (version) VALUES ('000_init_data_version');