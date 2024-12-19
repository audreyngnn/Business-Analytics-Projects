start_time <- proc.time()
x <- 1
y <- 1
z <- x + y
z
end_time <- proc.time()

end_time - start_time 

# Taking how long for it to finish running?

system.time({
x <- 1
y <- 1
z <- x + y
z
})


