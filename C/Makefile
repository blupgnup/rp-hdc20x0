CC = gcc
CFLAGS = -Wall -g

TARGET = test_HDC20X0

all: $(TARGET)

$(TARGET): $(TARGET).c C_HDC20X0.o
		$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c C_HDC20X0.o

C_HDC20X0.o: C_HDC20X0.c C_HDC20X0.h
		$(CC) $(CFLAGS) -c -g C_HDC20X0.c
clean:
		$(RM) $(TARGET) *.o
