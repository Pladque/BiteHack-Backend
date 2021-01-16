#include<bits/stdc++.h>
using namespace std;

class entry
{
public:

    int ID;
    int tagsComp;
    int wordsComp;
    vector<string>tags;
    vector<string>words;
    entry(vector<string> &t, vector<string> &w, int id)
    {
        tags=t;
        words=w;
        tagsComp = 0;
        wordsComp = 0;
        ID = id;
    }
};

bool compareByTags(const entry &a, const entry &b)
{
    if(a.tagsComp == b.tagsComp)
    {
        return a.wordsComp > b.wordsComp;
    }
    else
    {
        return a.tagsComp > b.tagsComp;
    }
}

bool compareByWords(const entry &a, const entry &b)
{
    if(a.wordsComp == b.wordsComp)
    {
        return a.tagsComp > b.tagsComp;
    }
    else
    {
        return a.wordsComp > b.wordsComp;
    }
}

int main(int argc, char* argv[])    //czytanie dwoch plikow do maina
{
    //ogolne wejscie plikow

    FILE *f1 = fopen(argv[1], "rt");    //plik wejsciowy z zapytaniem i archiwum
    FILE *f2 = fopen(argv[2], "wt");    //plik wyjsciowy
    char *a = argv[3];  //tryb wyszukiwania: 1 - tagi wazniejsze, 2 - tekst wazniejszy
    char *b = argv[4];   //maksymalna ilosc rekordow na wyszukiwanie
    int mode = atoi(a);
    int maxResult = atoi(b);

    //wczytywanie wejscia

    char c;
    int counter = 0;
    vector<string>tag,word;
    string x;
    vector<entry>tab;
    c = fgetc(f1);

    while(true) //petla do czytania wejscia
    {
        if (c == EOF)
        {
            break;
        }
        while(c != '\n')    //czytanie tagow
        {
            if(c == ' ')
            {
                tag.push_back(x);
                x.clear();
            }
            else
            {
                x += c;
            }
            c = fgetc(f1);
        }
        if(x.size() > 0)
        {
            tag.push_back(x);
        }
        x.clear();

        c = fgetc(f1); //czytanie slow
        while(c != '\n')
        {
            if(c == EOF)
            {
                break;
            }
            if(c == ' ')
            {
                word.push_back(x);
                x.clear();
            }
            else
            {
                x += c;
            }
            c = fgetc(f1);
        }
        if(x.size() > 0)
        {
            word.push_back(x);
        }
        entry obj(tag, word, counter); //wbijanie obiektow klasy entry na tablice tab
        if(counter==0)
        {
            obj.tagsComp=-1;
            obj.wordsComp=-1;
        }
        tab.push_back(obj);
        x.clear();
        tag.clear();
        word.clear();
        if(c == EOF)
        {
            break;
        }
        c = fgetc(f1);
        counter++;
    }

    //liczenie tags i words compatibility

    for(int i=1 ; i<tab.size() ; i++)
    {
        for(int j=0 ; j<tab[i].tags.size(); j++)    //tags compatibility
        {
            for(int k=0 ; k<tab[0].tags.size(); k++)
            {
                if(tab[i].tags[j] == tab[0].tags[k])
                {
                    tab[i].tagsComp++;
                }
            }
        }
        for(int j=0 ; j<tab[i].words.size(); j++)    //words compatibility
        {
            for(int k=0 ; k<tab[0].words.size(); k++)
            {
                if(tab[i].words[j] == tab[0].words[k])
                {
                    tab[i].wordsComp++;
                }
            }
        }
    }

    //sortowanie wzgledem trybu wybranego

    if(mode == 1)
    {
        sort(tab.begin(), tab.end(), compareByTags);
    }
    if(mode == 2)
    {
        sort(tab.begin(), tab.end(), compareByWords);
    }

    //wypisywanie ID do pliku

    int i = 0;
    while(i < maxResult)
    {
        if(mode == 1)
        {
            if(tab[i].tagsComp <= 0)
            {
                break;
            }
        }
        if(mode == 2)
        {
            if(tab[i].wordsComp <= 0)
            {
                break;
            }
        }
        fprintf(f2,"%d\n",tab[i].ID);
        i++;
    }
}
