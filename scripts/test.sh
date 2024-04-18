printf "==3DBAG\n"
\time python load_cityjson.py ../data/3DBAG.city.json
\time python load_cityjsonseq.py ../data/3DBAG.city.jsonl

printf "==Helsinki\n"
\time python load_cityjson.py ../data/Helsinki.city.json
\time python load_cityjsonseq.py ../data/Helsinki.city.jsonl

printf "==Helsinki_tex\n"
\time python load_cityjson.py ../data/Helsinki_tex.city.json
\time python load_cityjsonseq.py ../data/Helsinki_tex.city.jsonl

printf "==Ingolstadt\n"
\time python load_cityjson.py ../data/Ingolstadt.city.json
\time python load_cityjsonseq.py ../data/Ingolstadt.city.jsonl

printf "==Montréal\n"
\time python load_cityjson.py ../data/Montréal.city.json
\time python load_cityjsonseq.py ../data/Montréal.city.jsonl

printf "==NYC\n"
\time python load_cityjson.py ../data/NYC.json
\time python load_cityjsonseq.py ../data/NYC.jsonl

printf "==Railway\n"
\time python load_cityjson.py ../data/Railway.city.json
\time python load_cityjsonseq.py ../data/Railway.city.jsonl

printf "==Rotterdam\n"
\time python load_cityjson.py ../data/Rotterdam.json
\time python load_cityjsonseq.py ../data/Rotterdam.jsonl

printf "==Vienna\n"
\time python load_cityjson.py ../data/Vienna.city.json
\time python load_cityjsonseq.py ../data/Vienna.city.jsonl

printf "==Zurich\n"
\time python load_cityjson.py ../data/Zurich.city.json
\time python load_cityjsonseq.py ../data/Zurich.city.jsonl
