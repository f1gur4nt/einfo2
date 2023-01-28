
import os
import sys

email = sys.argv[1]

def correios(email):
  try:
    cmd = '''curl -q -s -X POST "https://apps.correios.com.br/idCorreios/naocadastrado/cadastrar-usuario.jsf?cid=1" -H "Cookie: JSESSIONID=5VasqIdoD4etMj7MoStgsh3M.5c6b2d0e-cbd6-322e-97e8-c77ec7459ef0; app-%3FINTERNO%3Fpool_proxy_svp_int_443=LBFIAIAK; sto-id-%3FEXTERNO_2%3Fpool_Proxy_reverso_Apps_443=MOABKIMA; sto-id-%3FEXTERNO_2%3Fpool_Apps_idCorreios_443=MOABKIMA" -d "formCadastrarUsuarioExterno=formCadastrarUsuarioExterno&formCadastrarUsuarioExterno:habilitaContrato=false&formCadastrarUsuarioExterno:clienteComContratoAtivoNoErp=false&formCadastrarUsuarioExterno:contratoExistenteNoErp=false&formCadastrarUsuarioExterno:contratoPertenceAoCliente=false&formCadastrarUsuarioExterno:cnpjExistenteNoErp=false&formCadastrarUsuarioExterno:exibeCamposAdicionais=false&formCadastrarUsuarioExterno:campoCPF=19949199291&formCadastrarUsuarioExterno:campoNome=kakxmam+makfkakk+akckkakk+akckkakx+&formCadastrarUsuarioExterno:campoDtNascimento=12/09/2002&formCadastrarUsuarioExterno:campoEmail=joao@gmail.com&formCadastrarUsuarioExterno:campoConfirmEmail=joao@gmail.com&formCadastrarUsuarioExterno:campoEmailAlternativo=Seupai@gmail.com&formCadastrarUsuarioExterno:campoIdCorreios=akkfkakckks&formCadastrarUsuarioExterno:campoSenha=asdfghjk123&formCadastrarUsuarioExterno:campoConfirmSenha=asdfghjk123&formCadastrarUsuarioExterno:CaptchaID=&formCadastrarUsuarioExterno:campoIdentficacaoEndereco=Minha+casa&formCadastrarUsuarioExterno:comboPais=+++++++BR+&formCadastrarUsuarioExterno:campoCep=65160-000&formCadastrarUsuarioExterno:campoEndereco=Mamsmam&formCadastrarUsuarioExterno:campoNumero=98293&formCadastrarUsuarioExterno:campoComplemento=Majxkakzksk&formCadastrarUsuarioExterno:campoBairro=Akkdkaksks+&formCadastrarUsuarioExterno:campoDddFixo=55&formCadastrarUsuarioExterno:campoFoneFixo=2939-9129&formCadastrarUsuarioExterno:campoDddMovel=29&formCadastrarUsuarioExterno:campoFoneCel=29391-9929&formCadastrarUsuarioExterno:campoAceite=on&javax.faces.ViewState=3792878007139773151:2155826375124282844&formCadastrarUsuarioExterno:j_idt79=formCadastrarUsuarioExterno:j_idt79&VALIDATE=true" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"'''.replace("joao@gmail.com",email)
    out = os.popen(cmd).read()
    if "O e-mail informado j" in out:
      print("Found")
  except:
    None

correios(email)
