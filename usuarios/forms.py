from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Larissa Sef" 
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome do cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Larissa Sef" 
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: larissa@exemail.com"
            }
        )
    )
    senha_cadastro=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    confirma_senha_cadastro=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme sua senha"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserrir espaços dentro do campo em destaque")
            else:
                return nome
