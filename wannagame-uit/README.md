# WANNAGAME

*Warning: Engrisk. Sorry about that, I'll make it better next time*

## Do I need to pay for professional versions? (200 pts)

Purpose: Find license key, so we need to analyze `checkLicense()` function.

Source `checkLicense()`:

```c
__int64 __fastcall checkLicense(__int64 key, __int64 key_, __int64 sth_equal_0)
{
  unsigned int i; // ebx
  __int64 hexcode_key; // rbp
  __int64 result; // rax
  int v6; // er10
  signed int *value_after_mapping; // rax

  i = 0;
  hexcode_key = hexdecode((const char *)key, key_, sth_equal_0);
  while ( 1 )
  {
    if ( (unsigned int)checksum(hexcode_key, i, 5) )
    {
      if ( (unsigned int)checksum(hexcode_key, 5 * i, 1) )
      {
        value_after_mapping = (signed int *)mapping(hexcode_key, v6, 5LL);
        result = check_part(
                   i,
                   *value_after_mapping,
                   value_after_mapping[1],
                   value_after_mapping[2],
                   value_after_mapping[3]);
        if ( !(_DWORD)result )
          break;
      }
    }
    if ( ++i == 5 )
      return 1LL;
  }
  return result;
}
```

After analyze:
+ We'll know `hexdecode()` function converts each 2 char from input to hexcode and make them to array. Example: `input='DEADBEEF', output=[0xDE, 0xAD, 0xBE, 0xEF]`.

+ Value of that array with pass to `checksum()` function twice times.

+ `mapping()` function converts each value of this array to ordinal number which value in string `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#`

+ `check_part()` function get each value and check with specific condition.

Solve `check_part()`. [checkpart.py](/wannagame-uit/re3-doIneed/checkpart.py)

Solve `mapping()`: I do it manually

Solve `checksum()`. [checksum.py](/wannagame-uit/re3-doIneed/checksum.py)

License: `3232300b3b66313f3951387e366919396367407d551e5e1b0e`

![flag.png](/wannagame-uit/re3-doIneed/flag.png)

## It is simple, but not easy (200 pts)

Stack overflow at function get input, so we just need to use gadget to take down this challenge.

Payload: [payload.py](/wannagame-uit/pwn2-itiss1mple/payload.py)

![flag.png](/wannagame-uit/pwn2-itiss1mple/flag.png)
