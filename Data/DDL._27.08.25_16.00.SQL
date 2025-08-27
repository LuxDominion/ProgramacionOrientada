CREATE TABLE IF NOT EXITS nacionalidad (
    id_nacionalidad INT NOT NILL AUTO_INCREMENT,
    pais VARCHAR(50) NOT NILL,
    nacionalidad VARCHAR(50) NOT NILL,
    CONSTRAINT PK_nacionalidad PRIMARY KEY (id_nacionalidad)
);

CREATE TABLE IF NOT EXITS autor (
    id_autor INT NOT NILL AUTO_INCREMENT,
    nombre_autor VARCHAR(100) NOT NILL,
    pseudonimo VARCHAR(100) NULL,
    id_nacionalidad INT NOT NILL,
    CONSTRAINT PK_autor PRIMARY KEY (id_autor),
    CONSTRAINT FK_autor_nacionalidad FOREING KEY (id_nacionalidad) REFERENCES 
)