import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Button } from '@/components/ui/button'

export default function RegisterPage() {
  return (
    <form className="space-y-4">
      <div>
        <Label htmlFor="name">Name</Label>
        <Input id="name" type="text" placeholder="John Doe" />
      </div>
      <div>
        <Label htmlFor="email">Email</Label>
        <Input id="email" type="email" placeholder="you@example.com" />
      </div>
      <div>
        <Label htmlFor="password">Password</Label>
        <Input id="password" type="password" placeholder="••••••••" />
      </div>
      <Button type="submit" className="w-full">Register</Button>
    </form>
  )
}

