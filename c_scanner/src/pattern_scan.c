// pattern_scan.c - small C helper to scan for known unsafe APIs quickly
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){
    if(argc<2){ fprintf(stderr, "usage: pattern_scan <file>\n"); return 2; }
    const char *path = argv[1];
    FILE *f = fopen(path, "r");
    if(!f){ perror("fopen"); return 2; }
    char buf[4096];
    int lineno=0;
    while(fgets(buf, sizeof(buf), f)){
        lineno++;
        if(strstr(buf, "gets(") || strstr(buf, "strcpy(") || strstr(buf, "system(")){
            printf("%d: %s", lineno, buf);
        }
    }
    fclose(f);
    return 0;
}
