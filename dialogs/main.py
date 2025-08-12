#===================================
#
#===================================
START_DIALOG = {
    "initial": {
        "id": 0,
        "texts": [
            "Você faz parte de uma tripulação espacial...",
            "Sua missão era simples, visitar Zeres,",
            "um planeta em um sistema distante onde uma",
            "base de pesquisa militar foi instaurada...",
            "Há um mês, a sede de comunicações perdeu",
            "contato total com a base de pesquisas...",
            "Uma missão de reconhecimento foi orquestrada",
            "as pressas e você foi escolhido graças a suas",
            "habilidades com..."
        ],
        "options": {
            "Mecânica": {"id": 0, "choice": "_class_chosed"},
            "Química": {"id": 1, "choice": "_class_chosed"},
            "Combate": {"id": 2, "choice": "_class_chosed"},
        }
    },
    "_class_chosed": {
        "id": 1,
        "texts": [
            "Seus superiores se impressionaram com suas",
            "habilidades... A viagem será longa e o planeta",
            "desconhecido pode reservar muitos perigos...",
            "O que você pretender levar consigo??"
        ],
        "options": {
            "Conhecimento": {"id": 0, "choice": "_item_chosed"},
            "Proteção": {"id": 1, "choice": "_item_chosed"},
            "Sobrevivência": {"id": 2, "choice": "_item_chosed"},
            "Lembranças": {"id": 3, "choice": "_item_chosed"},
        }
    },
    "_item_chosed": {
        "id": 2,
        "texts": ["Muito bem..."],
        "options": {}
    },
}