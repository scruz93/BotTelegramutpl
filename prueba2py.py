from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Lista de preguntas
preguntas = [
    "1. ¿En qué semestre se inician las prácticas preprofesionales en Tecnologías de la Información (TI)?",
    "2. ¿Cuántas horas se realiza?",
    "3. ¿Cuántas postulaciones puedo hacer?",
    "4. ¿Puedo postular en empresas públicas?",
    "5. ¿Las prácticas son presenciales o virtuales?",
    "6. ¿Puedo postular más de una empresa?",
    "7. ¿Yo elijo la empresa para las prácticas?",
    "8. ¿Necesito carta de autorización para las prácticas?",
    "9. ¿Cuántas horas puedo hacer en la empresa de postulación?",
    "10. ¿Qué significa postulación interna y externa?"
]

# Respuestas predefinidas para cada pregunta
respuestas = [
    "Las prácticas preprofesionales se inician generalmente en el cuarto semestre según la carrera.",
    "Son 192 horas de prácticas en el practicum 1.",
    "Se puede hacer una postulación tanto interna como externa.",
    "Sí, se puede postular en una empresa pública.",
    "Las prácticas pueden ser virtuales, presenciales o mixtas según la empresa.",
    "No, solo se puede hacer una postulación por empresa.",
    "Sí, tú eliges la empresa donde realizar las prácticas o si no la universidad te ofrece los lugares con convenios.",
    "Si la empresa lo solicita, la universidad junto con los docentes te ayudarán.",
    "Normalmente, puedes hacer hasta 20 horas semanales en la empresa de postulación.",
    "La postulación interna es cuando se realiza dentro de la universidad, mientras que la externa es para empresas fuera de la universidad."
]

# Función para crear botones con respuestas
def generar_botones(index):
    keyboard = [
        [InlineKeyboardButton("Ver respuesta", callback_data=str(index))]
    ]
    return InlineKeyboardMarkup(keyboard)

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "¡Hola! Soy un chatbot de prácticas universitarias. Escribe /preguntas para comenzar."
    )

# Función para el comando /preguntas
async def preguntas_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(preguntas)):
        # Enviar la pregunta con un botón para ver la respuesta
        await update.message.reply_text(
            preguntas[i],
            reply_markup=generar_botones(i)  # Crear botones para la pregunta
        )

# Función para manejar las respuestas al hacer clic en los botones
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    question_index = int(query.data)  # Obtener el índice de la pregunta
    await query.answer()  # Necesario para confirmar que se recibió el clic
    await query.edit_message_text(  # Cambiar el mensaje de la pregunta por la respuesta
        text=f"{preguntas[question_index]}\n\n{respuestas[question_index]}"
    )

# Función para responder cuando el usuario diga "gracias"
async def gracias_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # El bot responderá con un mensaje de despedida cuando detecte "gracias"
    await update.message.reply_text(
        "¡De nada! 😊 ¡Que tengas un excelente día y mucho éxito en tus prácticas universitarias! 👋"
    )

# Configuración del bot
def main():
    # Reemplaza "YOUR_TOKEN" con el token de @BotFather
    application = Application.builder().token("7558093473:AAEB0zdso47D2yXYmYbVjUBl3m8R0M60gqw").build()

    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("preguntas", preguntas_handler))

    # Manejador de botones
    application.add_handler(CallbackQueryHandler(button_handler))

    # Manejador para la palabra "gracias" usando el filtro correcto
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('(?i)gracias'), gracias_handler))

    # Iniciar el bot
    print("Bot en ejecución...")
    application.run_polling()

if __name__ == '__main__':
    main()
