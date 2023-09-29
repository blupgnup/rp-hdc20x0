# Compiler and compiler flags
CXX := g++
CXXFLAGS := -Wall -Werror -Iinclude -fPIC

# Source and object files
SRC_DIR := src
SRC := $(wildcard $(SRC_DIR)/*.c)
OBJ := $(SRC:.c=.o)

# Library name and installation directory
LIBRARY_NAME := rp-hdc20x0
LIB_DIR := /opt/redpitaya/lib
INCLUDE_DIR := /opt/redpitaya/include/$(LIBRARY_NAME)

# Example source file
EXAMPLES_DIR := examples
EXAMPLE_SRC := $(EXAMPLES_DIR)/test_HDC20X0.c

# Targets
all: $(LIBRARY_NAME) $(EXAMPLE_SRC:.c=)

$(LIBRARY_NAME): $(OBJ)
	ar rcs lib$(LIBRARY_NAME).a $(OBJ)

%.o: %.c
	$(CXX) $(CXXFLAGS) -c $< -o $@

%: %.c
	$(CXX) $(CXXFLAGS) $< -o $@ -L. -l$(LIBRARY_NAME)

install: $(LIBRARY_NAME)
	cp lib$(LIBRARY_NAME).a $(LIB_DIR)
	mkdir -p $(INCLUDE_DIR)
	cp include/* $(INCLUDE_DIR)

clean:
	rm -f $(OBJ) lib$(LIBRARY_NAME).a $(EXAMPLE_SRC:.c=)

uninstall:
	rm -f $(LIB_DIR)/lib$(LIBRARY_NAME).a
	rm -f $(INCLUDE_DIR)/*
	rm -d $(INCLUDE_DIR)

.PHONY: all install clean uninstall

