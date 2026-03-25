import models
from database import SessionLocal
from _datetime import datetime

from routers import notes


def generate_weekly_report():
    db = SessionLocal()
    notes = db.query(models.Note).all()

    if not notes:
        print("Raporlanacak Herhangi Bir Not Bulunamadı")
        db.close()
        return

    date_str = datetime.today().strftime('%Y-%m-%d')
    filename = f'Haftalik_Rapor_{date_str}.md'

    with open(filename, 'w' , encoding="utf-8") as file:
        file.write(f"# DevDiary Haftalık Geliştirme Raporu ({date_str})\n\n")
        for note in notes:
            file.write(f'## {note.title}\n\n')
            file.write(f'**Mode:** {note.mode}\n\n')
            file.write(f'**Note:** {note.content}\n\n')

            if note.analysis:
                file.write(f'**Llama Analizi:** {note.analysis}\n\n')
                file.write('--------\n\n')

    print(f"Rapor Başarili {filename}")
    db.close()

if __name__ == "__main__":
    generate_weekly_report()


