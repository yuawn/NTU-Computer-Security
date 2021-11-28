# NTU Computer Security Fall 2019 - 台大 計算機安全
擔任台大大助教，與三週 Pwn 課程講師。

## 課程內容
### Week 1: Binary Exploitation - Basic

- Slide: [speakerdeck.com/yuawn/binary-exploitation-basic](https://speakerdeck.com/yuawn/binary-exploitation-basic)  
- Video: [youtu.be/U8N6aE-Nq-Q](https://youtu.be/U8N6aE-Nq-Q)
- Lab:
    - [bof](week1/exp/bof.py)
        - stack buffer overflow, overwrite return address
    - [orw](week1/exp/orw.py)
        - seccomp filter syscall, shellcode
- Homework:
    - [Casino](week1/exp/casino.py)
        - oob array access, GOT hijacking, shellcode

### Week 2: Binary Exploitation

- Slide: [speakerdeck.com/yuawn/binary-exploitation](https://speakerdeck.com/yuawn/binary-exploitation)  
- Video: [youtu.be/5D7tvxpSUUM](https://youtu.be/5D7tvxpSUUM)
- Lab:
    - [ROP](week2/exp/rop.py)
        - ROP bypass NX protection
    - [ret2plt](week2/exp/ret2plt.py)
        - Practice using plt functions
    - [ret2libc](week2/exp/ret2libc.py)
        - information leak, bypass ASLR, practice ret2libc technique
- Homework:
    - [Casino++](week2/exp/casino++.py)
        - oob array access, GOT hijacking, leak libc, ret2libc hijack plt function to system()

### Week 3: Heap Exploitation

- Slide: [speakerdeck.com/yuawn/heap-exploitation](https://speakerdeck.com/yuawn/heap-exploitation)  
- Video: [youtu.be/rMqvL9j0QaM](https://youtu.be/rMqvL9j0QaM)
- Lab:
    - [UAF](week3/exp/uaf.py)
        - Practice using UAF to leak address and exploit.
    - [Note](week3/exp/note.py)
        - double free, fastbin attack
    - [T-Note](week3/exp/t-note.py)
        - Tcache dup
- Homework:
    - [Election](week3/exp/election.py)
        - stack pivoting, ret2csu csu gadget
    - [Note++](week3/exp/note++.py)
        - off-by-one null byte overflow, fastbin dup, forge chunk size to leak libc, overwrite __malloc_hook, one gadget

## 課程題目 challenges
- 各 week 中 `src` 底下為題目原始碼
- 各 week 中 `exp` 底下為答案解法 exploits

### 環境 environment
- OS: ubuntu 18.04
- GCC: gcc (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0

### Build

```bash
cd week1 # week2 week3
docker-compose up -d
```

### Compile (如需自行重編題目 binary)

```bash
sudo apt install libseccomp-dev
make
```
