# Tkinter Appp

Questo è un programma per ottenere un logo random in formato PNG, a partire dalla libreria di loghi pre-realizzati https://github.com/FTurci/write-logos/tree/main/src/pngs.


Il programma è una semplice interfaccia `Tkinter`.


## Codice sorgente

Nella cartella `src` vi è il codice Python.

Per eseguire il programma, occorrono i moduli supplementari specificati nel file `requirements.txt`. Quindi, qualora non fossero installati, è necessario eseguire il seguente comando

```
pip install -r requirements.txt
```

Per eseguire il programma è quindi sufficiente eseguire

```
python RandomLogo.py         
```

### Note

Lo script non richiede l'installazione dei font, perché scarica immagini `png` localmente in file temporanei. È possibile salvare permanentemente un logo selezionato.
