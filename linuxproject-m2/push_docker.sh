   
# Build mdanwebfront image
cd mdanwebfront
docker build -t myrthedaniels/mdanwebfront:latest .

# Build mdanfastapi image
cd ../mdanfastapi
docker build -t myrthedaniels/mdanfastapi:latest .

# Build mdanpostgreSQL image (no custom Dockerfile)
cd ..
docker build -t myrthedaniels/mdanpostgresql:latest .



docker tag mdanwebfront:latest myrthedaniels/mdanwebfront:latest
   docker tag mdanfastapi:latest myrthedaniels/mdanfastapi:latest
   docker tag mdanpostgresql:latest myrthedaniels/mdanpostgresql:latest

