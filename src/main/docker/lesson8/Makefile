SUBJ_C?=BR
SUBJ_ST?=Sao Paulo
SUBJ_L?=Pompeia
SUBJ_O?=FATEC
SUBJ_OU?=FATEC Network
SUBJ_CN?=example.com


%.key:
	openssl genrsa -out $@ 4096

%.crt: %.key
	openssl req -new -x509 -days 3650 -key $< -out $@ -subj "/C=${SUBJ_C}/ST=${SUBJ_ST}/L=${SUBJ_L}/O=${SUBJ_O}/OU=${SUBJ_OU}/CN=${SUBJ_CN}"

%.pem: %.key %.crt 
	cat $^ > $@
