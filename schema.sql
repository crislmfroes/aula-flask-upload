create table Arquivo(
    cod serial primary key,
    caminho varchar(100)
);

create table ArquivoBinario(
    cod serial primary key,
    data bytea
);