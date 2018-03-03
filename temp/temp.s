    .data
msg1:
    .asciiz "Enter a number:"
msg2:
    .asciiz "The result is:"
eof:
    .asciiz "\n"


#main_function

    .data
    
main_ret_save:
    .word 4
    .text
    .globl main

main:
    sw $ra main_ret_save
    
    la $a0, msg1    #printf("Enter a number:");
    li $v0, 4
    syscall
    
    li $v0,5
    syscall         #scanf("%d",v0);
    
    
    
    jal   doub
    
    move $a0, $v0
    li $v0, 1
    syscall 
    
    lw $ra, main_ret_save
    jr $ra
    
    
    
#doub function:
    .data
    doub_ret_save:
        .space 4
    .text
doub:
    sw $ra, doub_ret_save

    mul  $v0,$v0,2
    lw $ra, doub_ret_save
    jr $ra
    
    
    
    
    
    
    
    
    
    
