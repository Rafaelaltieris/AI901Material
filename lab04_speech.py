"""
Lab 04 - Get started with AI Speech
Demonstração das 2 APIs principais:
- Speech-to-Text: usa o microfone do computador, transcreve a fala
- Text-to-Speech: sintetiza voz a partir de texto
Requer: microfone e auto-falante funcionando.
"""
import azure.cognitiveservices.speech as speechsdk

# Credenciais do recurso de Speech / Foundry
# IMPORTANTE: em produção, nunca deixe a chave hardcoded.
# Prefira variáveis de ambiente, Azure Key Vault ou Managed Identity.
speech_key = ""
speech_region = "eastus2"

# Configuração compartilhada para os dois serviços
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    region=speech_region,
)

# Define idioma para português brasileiro
speech_config.speech_recognition_language = "pt-BR"
speech_config.speech_synthesis_voice_name = "pt-BR-FranciscaNeural"


def speech_to_text():
    """Captura áudio do microfone e transcreve para texto."""
    print("Fale algo agora...")

    # Usa o microfone padrão do sistema como input
    audio_config = speechsdk.audio.AudioConfig(
        use_default_microphone=True,
    )

    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    # Reconhecimento único (uma frase só)
    result = recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Você disse:", result.text)
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Nenhuma fala foi reconhecida.")
        print(f"Detalhes: {result.no_match_details}")
        return None
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print(f"Cancelado: {cancellation.reason}")
        print(f"Detalhes do erro: {cancellation.error_details}")
        return None


def text_to_speech(text):
    """Sintetiza voz a partir de um texto."""
    # Usa o auto-falante padrão do sistema como output
    audio_config = speechsdk.audio.AudioOutputConfig(
        use_default_speaker=True,
    )

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    synthesizer.speak_text_async(text).get()


# Pipeline: ouve o aluno, depois fala de volta o que ouviu
texto = speech_to_text()

if texto:
    text_to_speech(f"Você disse {texto}")