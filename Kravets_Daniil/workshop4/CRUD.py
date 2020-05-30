from  database_connection import engine
from sqlalchemy.orm import sessionmaker
from models_create import OrderSong, Broadcast, Chain, Announcement, feedback, help, AnnouncementChain
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

song1 = OrderSong(
    song_name = 'Sleepwalking',
    song_artist = 'Bring Me The Horizon',
)

announ1 = Announcement(
    announcement_text = 'Hi!'
)

broadcast1 = Broadcast(
    broadcast_date = func.current_date()
)


session.add(song1)
session.commit()
session.add(announ1)
session.commit()
session.add(broadcast1)
session.commit()

song1_id = (session.query(OrderSong).filter(OrderSong.song_name == 'Sleepwalking')[0]).song_id
announ1_id = (session.query(Announcement).filter(Announcement.announcement_text == 'Hi!')[0]).announcement_id
broadcast1_id = (session.query(Broadcast).filter(Broadcast.broadcast_date == func.current_date())[0]).broadcast_id

order_chain = Chain(
    broadcast_id_fk = broadcast1_id,
    song_id = song1_id
)

announcement_chain = AnnouncementChain(
    broadcast_id_fk = broadcast1_id,
    announcement_id_fk = announ1_id
)

instances = [order_chain, announcement_chain]
for ins in instances:
    session.add(ins)
    session.commit()