# PlaidCTF 2019

## reee (150 pts)

In main:

```c
int __fastcall main(unsigned __int64 argc, char **argv, char **argv0)
{
  char *argv_; // ST20_8
  int result; // eax
  signed int j; // [rsp+18h] [rbp-28h]
  signed int i; // [rsp+1Ch] [rbp-24h]

  if ( (signed int)argc <= 1 )
  {
    argc = (unsigned __int64)"need a flag!";
    puts("need a flag!");
  }
  argv_ = argv[1];
  for ( i = 0; i <= 31336; ++i )
  {
    for ( j = 0; j <= 551; ++j )
    {
      argc = (unsigned int)*((char *)&raw_func + j);
      *((_BYTE *)&raw_func + j) = generate_func(argc); // decrypting begin at &raw_func
    }
  }
  if ( ((__int64 (__fastcall *)(unsigned __int64))raw_func)(argc) ) // execution raw_func()
    result = puts("Correct!");
  else
    result = puts("Wrong!");
  return result;
}
```

From main, we know all thing will be done in raw_func()

Unpacking raw_func() with gdb:

```sh
$ b*0x4006DB
$ r aaaa
$ dump binary memory raw_func 0x04006E5 0x04006E5+552
```

After reversing raw_func(), we got algorithm in raw_func() in [algorithm-in-reee.py](/plaid2020/reee/algorithm-in-reee.py)

Then using Z3 to solve. [solve.py](/plaid2020/reee/solve.py)

Flag: `pctf(ok_nothing_too_fancy_there!}`

## YOU wa SHOCKWAVE (250 pts)

![screenshot.png](/plaid2020/you-wa-SHOCKWAVE/screenshot.png)

After using google a bit, we know .dcr file is Lingo script. [1](https://reverseengineering.stackexchange.com/questions/14089/reverse-engineering-lingo-scripts-dcr-cct-files) [2](https://medium.com/@nosamu/a-tour-of-the-adobe-director-file-format-e375d1e063c0)

I got Lingo Script. [lingo-script](/plaid2020/you-wa-SHOCKWAVE/lingo-script.txt)

Solution: [solve.py](plaid2020/you-wa-SHOCKWAVE/solve.py)

Flag: `PCTF{Gr4ph1CS_D3SiGn_Is_tRUlY_My_Pas5ioN!}`
