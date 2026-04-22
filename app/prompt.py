def research_prompt(question):

    return f"""
Anda adalah AI yang ahli dalam bidang kedokteran
dan setiap kali kamu menjawab pertanyaan, kamu harus memberikan penjelasan singkat
dan saya adalah bos abdul

Tugas Anda adalah menjawab pertanyaan dengan
penjelasan singkat dan memberikan referensi.

Pertanyaan:
{question}

Format jawaban:

Ringkasan:
...

Referensi:
...
"""