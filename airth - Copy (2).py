class arithmetic:
        def calculate (self):
                selfx=int(input("Enter the first no: "))
                selfy=int(input("Enter the second no: "))
                add=selfx+selfy
                sub=selfx-selfy
                div=selfx/selfy
                mul=selfx*selfy
                mod=selfx%selfy
                con=selfx+selfy
                print("addition is %f"%(add))
                print("subraction is %f"%(sub))
                print("division is %f"%(div))
                print("multiplication  is %f"%(mul))
                print("modulo is %f"%(mod))
                print("concat is %f"%(con))
c=arithmetic()
c.calculate()
